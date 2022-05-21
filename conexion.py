# -*- coding: utf-8 -*-

import sys
from psycopg2 import pool

import conf
from logger_base import log


class Conexion:
    _DATABASE = conf.DATABASE
    _USERNAME = conf.USERNAME
    _PASSWORD = conf.PASSWORD
    _DB_PORT = conf.DBPORT
    _HOST = conf.DB_PORT
    _MIN_CON = conf.MIN_CON
    _MAX_CON = conf.MAX_CON
    _pool = None
    
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON, 
                    host=cls._HOST, user=cls._USERNAME, password=cls._PASSWORD,
                    port=cls._DB_PORT, dbname=cls._DATABASE
                )
                log.debug(f'Creacion de pool exitosa {cls._pool}')
                return cls._pool
            except Exception as err:
                log.error(f'Ocurrio un error al obtener el pool {err}')
                sys.exit()
        return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')


    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == '__main__':
    conexion = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion)
    Conexion.cerrarConexiones()
