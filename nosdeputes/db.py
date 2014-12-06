# -*- coding: utf-8 -*-
from settings import db_config

mysql_db = {
    'host': 'localhost',
    'user': db_config.get('nosdeputes', 'user'),
    'passwd': db_config.get('nosdeputes', 'passwd'),
    'db': db_config.get('nosdeputes', 'db'),
    'port': 3306,
    'use_unicode': True,
    'charset': 'utf8',
}