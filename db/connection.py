import sqlite3
from config.db_config import DB_PATH

class Database:
    _instance = None

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Database()
        return cls._instance

    def get_connection(self):
        return self.conn
