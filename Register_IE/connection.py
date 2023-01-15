import sqlite3
from config import *


class Connection:
    def __init__(self, querySQL):
        self.con = sqlite3.connect(ORIGIN_DATA) #Connection, check python SQL library
        self.cur = self.con.cursor()
        self.res = self.cur.execute(querySQL)