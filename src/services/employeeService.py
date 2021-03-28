import psycopg2

from services import configurationService


class EmployeeService:
    def __init__(self):
        try:
            host = configurationService.config['PostgreSQL']['Host']
            port = configurationService.config['PostgreSQL']['Port']
            db = configurationService.config['PostgreSQL']['Database']
            self.user = configurationService.config['PostgreSQL']['User']
            password = configurationService.config['PostgreSQL']['Password']
            self.schema = configurationService.config['PostgreSQL']['Schema']
            self.table = configurationService.config['PostgreSQL']['Tables']['Employees']
            self.connection_string = f'host={host} port={port} dbname={db} user={self.user} password={password}'
            self.connection = psycopg2.connect(self.connection_string)
            self.cur = self.connection.cursor()
            self._alive = True

            if (not self.check_existing_table()):
                self.create_table()
                print('Table created')

        except Exception as e:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)
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

    def check_existing_table(self):
        sql = f'''SELECT true
        FROM information_schema."tables"
        WHERE table_schema = '{self.schema}'
        AND table_name = '{self.table}';
        '''
        self.cur.execute(sql)
        records = self.cur.fetchall()

        try:
            if (records[0][0] == True):
                return True
        except:
            return False

    def create_table(self):
        sql = f'''CREATE TABLE {self.schema}.{self.table}
        (
            id BIGSERIAL PRIMARY KEY,
            name character varying(64) NOT NULL,
            position character varying(32) NOT NULL,
            salary integer NOT NULL,
            "managerId" integer
        )

        TABLESPACE pg_default;

        ALTER TABLE {self.schema}.{self.table}
            OWNER to "{self.user}";

        COMMIT;'''
        self.cur.execute(sql)

    def get_employee(self, id: int):
        self.cur.execute(
            f'SELECT * from {self.schema}.{self.table} WHERE id = {id}')
        result = self.cur.fetchall()
        return result

    def get_all_employees(self):
        return None

    def create_employee(self):
        return None

    def delete_employee(self):
        return None
