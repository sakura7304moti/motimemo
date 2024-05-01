import sqlite3
from const import sqlite_db

dbname = sqlite_db()
"""
Tables
"""
class Dialy():
    """
    日記
    """
    id : int # primary key
    title : str
    detail : str
    date : str

class Photo():
    """
    写真
    保存先 : photos / id.元のファイル名.jpg?png?jpeg?
    """
    id : int # primary key
    dialy_id : int # reference from Dialy.id
    file_name : str # original file name

"""
Queries
"""
