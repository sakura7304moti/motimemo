import sqlite3
from motimemo.src.const import sqlite_db

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
    """
    id : int # primary key
    dialy_id : int # reference from Dialy.id
    file_name : str # original file name

"""
Queries
"""
class QueryModel():
    def make_table():
        """
        テーブルの作成
        """
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

        dialy_query = """
        CREATE TABLE IF NOT EXISTS dialy(
            id INTEGER PRIMARY KEY,
            title STRING,
            detail STRING,
            date STRING
        )
        """

        photo_query = """
        CREATE TABLE IF NOT EXISTS photo(
            id INTEGER PRIMARY KEY,
            dialy_id INTEGER REFERENCES dialy(id),
            file_name STRING
        )
        """

        cur.execute(dialy_query)
        cur.execute(photo_query)

        conn.commit()
        conn.close()


    def create(
            title:str,
            detail:str,
            date:str,
            file_names:list[str]
    ):
        """
        日記の作成
        """
        # dialy insert
        conn = sqlite3.connect(dbname)
        cursor = conn.cursor()

        dialy_query = """
        INSERT INTO dialy (
            title,
            detail,
            date
        ) 
        VALUES (:title, :detail, :date)
        """

        dialy_args = {
            "title" : title,
            "detail" : detail,
            "date" : date
        }

        cursor.execute(dialy_query, dialy_args)
        conn.commit()

        # get max id record
        max_id_query = """
        SELECT id FROM dialy where id = max(id)
        """
        cursor.execute(max_id_query)
        record = cursor.fetchone()
        max_id = record[0]

        # photo insert
        dialy_query = """
        INSERT INTO photo (
            dialy_id,
            file_name
        ) 
        VALUES (:dialy_id, file_name)
        """
        for file_name in file_names:
            cursor.execute(dialy_query, {
                "dialy_id" : max_id,
                "file_name" : file_name
            })
        conn.commit()
        conn.close()