import bme280
import gy302
from connect_ms import mssql

# 環境データを各センサから取得する
def read_env_data():
    bme = get_bme_data()

    temp = bme[0]
    hum = bme[1]
    pres = bme[2]
    illum = get_gy_data()

    # データベースに書き込む
    regist_data(temp, hum, pres, illum)

    # データベースに書き込む
def regist_data(temp, hum, pres, illum):
    # MSSQL接続クラスに渡す
    mssql.insert_record(round(temp, 2), round(hum, 2), round(pres, 2), illum)

# bme280から温度、湿度、気圧を取得
def get_bme_data():
    return  bme280.readData()

def get_gy_data():
    return gy302.main()

if __name__ == '__main__':
	try:
		read_env_data()
	except KeyboardInterrupt:
		pass
