import pyodbc
import datetime

class mssql:
    @classmethod
    def insert_record(self, getday, temp, hum, pres): 
        # 接続情報 自分の環境に合わせて書き換える
        database = '*******'
        user = '*******'
        password = '*******'
        dsn = '*****'
        
        # 接続文字列作成
        con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user, password, database)
        # DBに接続
        cnxn = pyodbc.connect(con_string)
        #　カーソル作成
        cursor = cnxn.cursor()
        # insert文
        sql = """INSERT INTO t01_environment_data(register_at, temperature, humidity, pressure) VALUES(?, ?, ?, ?)"""
        try:
            # インサート
            cursor.execute(sql, getday, temp, hum, pres)
            cursor.commit()
            print("Insert Success! :) \n")
        except:
            print("Insert Failed :( \n")
            return
        
        print("result...")
        cursor.execute("SELECT * FROM environment_data")
        row = cursor.fetchone()
        while row:
            print(str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
            row = cursor.fetchone()

        print('OK')
        
if __name__ == '__main__':
    insert = mssql()
    insert.insert_record(datetime.datetime.today(), 10.0, 10.0, 10.0)
