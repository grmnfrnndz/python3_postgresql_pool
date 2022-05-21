# -*- coding: utf-8 -*-

from conexion import Conexion
from logger_base import log


class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug(f'Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_except, valor_except, traceback_except):
        log.debug(f'Se ejecuta metodo __exit__')
        if valor_except:
            self._conexion.rollback()
            log.error(f'Ocurrio una exception - rollback: {valor_except} {tipo_except} {traceback_except}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM persona;')
        log.debug(cursor.fetchall())