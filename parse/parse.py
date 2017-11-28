import feedparser

# 取得ページ設定
rss_url = "http://weather.livedoor.com/forecast/rss/area/050010.xml"
# パースする
weather = feedparser.parse(rss_url)

for entry in weather["entries"]:
    print(entry["title"])
    print(entry["link"])
