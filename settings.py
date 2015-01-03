# -*- coding: utf-8 -*-

import os
import ConfigParser

db_config = ConfigParser.ConfigParser()

if os.path.isfile('db.cfg'):
    db_config.read('db.cfg')
else:
    db_config.read('db_config.sample')

