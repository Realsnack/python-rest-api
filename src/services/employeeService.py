import psycopg2
from fastapi.logger import logger


class EmployeeService:
    def __init__(self):
        try:
            self.connection_string = f'host=postgredb.msvacina.cz port=5432 dbname=python-rest user=python-rest_app password=Pythonheslo'
            self.connection = psycopg2.connect(self.connection_string)
            self.cur = self.connection.cursor()
            self._alive = True
            logger.info('Connection to postgres is now alive')
        except:
            logger.warning('Connection to postgres is not alive')
            self._alive = False

    def get_postgres_status(self):
        if (self._alive == False):
            logger.info('Trying to reconnect to postgres')
            self.get_connection()

        try:
            self.cur.execute('SELECT NOW()')
            pgStatus = True
            logger.info('Postgres is up')
        except:
            pgStatus = False
            logger.warning('Postgres is down')
            self._alive = False

        logger.info(f'Returning status: {pgStatus}')
        return pgStatus

    def get_connection(self):
        try:
            self.connection = psycopg2.connect(self.connection_string)
            self.cur = self.connection.cursor()
            self._alive = True
            logger.info('Connection to postgres is now alive')
        except:
            self._alive = False
            logger.warning('Connection to postgres is not alive')
