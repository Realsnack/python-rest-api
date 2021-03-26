import psycopg2

class EmployeeService:
    def __init__(self):
        try:
            self.connection_string = f'host=postgredb.msvacina.cz port=5432 dbname=python-rest user=python-rest_app password=Pythonheslo'
            self.connection = psycopg2.connect(self.connection_string)
            self.cur = self.connection.cursor()
            self._alive = True
        except:
            self._alive = False

    def get_postgres_status(self):
        if (self._alive == False):
            self.get_connection()

        try:
            self.cur.execute('SELECT NOW()')
            pgStatus = True
        except:
            pgStatus = False
            self._alive = False

        return pgStatus

    def get_connection(self):
        try:
            self.connection = psycopg2.connect(self.connection_string)
            self.cur = self.connection.cursor()
            self._alive = True
        except:
            self._alive = False
