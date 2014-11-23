# -*- coding: utf-8 -*-

import csv
import codecs
import cStringIO


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")


class UnicodeReader(object):
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", fieldnames=None, **kwds):
        f = UTF8Recoder(f, encoding)
        self.encoding = encoding
        self.fieldnames = fieldnames
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        decoded_rows = [unicode(s, self.encoding) for s in row]

        if self.fieldnames is not None:
            return dict([(self.fieldnames[i], s) for i, s in enumerate(decoded_rows)])
        else:
            return decoded_rows

    def __iter__(self):
        return self


class UnicodeWriter(object):
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoding = encoding

    def writerow(self, row):
        self.writer.writerow([s.encode(self.encoding) for s in row])
        data = self.queue.getvalue()
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)