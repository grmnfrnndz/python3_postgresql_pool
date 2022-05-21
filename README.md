# Python3 PostgreSQL POOL

Simple context manager de pool de conexiones a postgreSQL.



```
    # instalar psycopg2
    pip install psycopg2
```

## Renombrar Archivo


example_conf.py -> conf.py

## completar las variables con los valores correctos

```
DATABASE = ''
USERNAME = ''
PASSWORD = ''
DB_PORT = '5432'
HOST = '127.0.0.1'
MIN_CON = 1
MAX_CON = 5

```

### Ejemplo de uso

```

from conexion import Conexion
from logger_base import log

with CursorDelPool() as cursor:
    cursor.execute('SELECT * FROM persona;')
```