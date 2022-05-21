# -*- coding: utf-8 -*-

import logging as log

log.basicConfig(level=log.DEBUG,
    format='%(asctime)s : %(levelname)s [ %(filename)s: %(lineno)s ] %(message)s',
    datefmt='%I/%M/%S %P',
    handlers=[
        log.FileHandler('err_data.log'),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('message')
