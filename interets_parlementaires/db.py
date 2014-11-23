# -*- coding: utf-8 -*-
from settings import db_config

mysql_db = {
    'host': 'localhost',
    'user': db_config.get('interets_parlementaires', 'user'),
    'passwd': db_config.get('interets_parlementaires', 'passwd'),
    'db': db_config.get('interets_parlementaires', 'db'),
    'port': 3306,
    'use_unicode': True,
    'charset': 'utf8',
}