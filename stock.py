import urllib
import re
import json

htmlfile = urllib.urlopen("http://www.bloomberg.com/markets/watchlist/recent-ticker/AAPL:US")
# htmltext = htmlfile.read()

# regex = '<span id="ref_[^.]*_l">(.+?)</span>'

# pattern = re.compile(regex)

# price = re.findall(pattern, htmltext)

data = json.load(htmlfile)

print data["last_price"]