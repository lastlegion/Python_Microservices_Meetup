import logging
import sqlite3

class TodoRepository:
    def __init__(self, db):
        self.db = db
        self.initialize()


    def initialize(self):
        items_table = '''
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                status TEXT NOT NULL
            )
        '''
        logging.info('Creating tables...')
        try:
            connection = sqlite3.connect(self.db)
            connection.execute(items_table)
        except Exception as e:
            logging.fatal(f'Couldnot intialize table {e}')

    def get_all_todos(self):
        query = '''
            SELECT * FROM items
        '''
        rows = None
        try:
            connection = sqlite3.connect(self.db)
            c = connection.cursor()
            c.execute(query)
            rows = c.fetchall()
        except Exception as e:
            logging.warning(f'Repository error: {e}')
        return rows

    def add_todo(self, description: str, status: str):
        query = f'''
            INSERT INTO items(description, status) VALUES("{description}", "{status}")
        '''
        id_ = None
        try:
            connection = sqlite3.connect(self.db)
            c = connection.cursor()
            c.execute(query)
            connection.commit()
            id_ = c.lastrowid()
        except Exception as e:
            logging.warning(f'Repository error: {e}')
        return {
            'description': description,
            'status': status,
            'id': id_
        }

    def update_todo(self, id_: int, description: str, status: str):
        query = f'''
            UPDATE items SET status="{status}", description="{description}" WHERE id={id_}
        '''
        print(query)
        try:
            connection = sqlite3.connect(self.db)
            c = connection.cursor()
            c.execute(query)
            connection.commit()
            print('all done!!')
        except Exception as e:
            logging.warning(f'Repository error: {e}')
        return {
            'description': description,
            'id': id_,
            'status': status
        }

    def delete_todo(self, id_: int):
        query = f'''
            DELETE FROM items WHERE id={id_}
        '''
        try:
            connection = sqlite3.connect(self.db)
            c = connection.cursor()
            c.execute(query)
            connection.commit()
        except Exception as e:
            logging.warning(f'Repository error: {e}')
