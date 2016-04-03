# -*- coding: utf-8 -*-

from settings import db_config

mysql_db = {
    'db': db_config.get('nossenateurs', 'db'),
    'kwargs': {
        'host': 'localhost',
        'user': db_config.get('nossenateurs', 'user'),
        'passwd': db_config.get('nossenateurs', 'passwd'),
        'port': 3306,
        'use_unicode': True,
        'charset': 'utf8',
    }
}