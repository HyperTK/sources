# 環境データ取得プログラム
Raspberry Pi 3 Model Bを使用して、温度、湿度、気圧、照度のデータを取得します。
プログラムのご使用は自由ですが、それに伴う基板、センサの破損の責任は負いません。
自己責任にてご利用ください。

## 各ファイルの説明
- env_data.py  
メインプログラムです。これを実行すると接続されているセンサからデータを取得します。  
自作したプログラムです。

- bme280.py  
温度、湿度、気圧をbme280というセンサから取得します。プログラムはスイッチサイエンス様が提供しているものを少し改造して使用しています。  
<https://github.com/SWITCHSCIENCE/BME280/blob/master/Python27/bme280_sample.py>

- gy302.py  
照度をGY-302というセンサから取得します。プログラムは海外のサイトに掲載されていたものを少し改造して使用しています。  
<https://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/>

- connect_ms.py  
Microsoft Azure上のSQLデータベースにセンサから取得した値をインサートします。
自作したプログラムです。ご自身の環境に合わせて書き換えてください。  
参考  
Azure上にサーバ環境を用意する  
<http://tk-thunder.hateblo.jp/entry/2018/02/12/200016>
