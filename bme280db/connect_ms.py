import pyodbc

class mssql:
    @classmethod
    def insert_record(self, temp, hum, pres):
        # 接続情報 自分の環境に合わせて書き換える
        database = '*******'
        user = '*******'
        password = '*******'
        dsn = '*****'

        # 接続文字列作成
        con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
        # DBに接続
        cnxn = pyodbc.connect(con_string)
        # カーソル作成
        cursor = cnxn.cursor()
        # insert文
        sql = """INSERT INTO テーブル名(temperature, humidity, pressure) VALUES(?, ?, ?)"""
        try:
            # インサート
            cursor.execute(sql, temp, hum, pres)
            cursor.commit()
            print("Insert Success! :) \n")
        except:
            print("Insert Failed :( \n")
            return

if __name__ == '__main__':
