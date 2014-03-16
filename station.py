import urllib
import re

	
url = "http://www.pandora.com/profile/stations/billgeorge1"
# url = "http://www.pandora.com/content/station_track_thumbs?stationId=1026742826420861487&page=true&posFeedbackStartIndex=5"
# url = "http://www.pandora.com/content/stations?startIndex=0&webname=billgeorge1"
regex = 'href=(.+?)>Classical for Studying Radio</a>'
# regex = '<a href="/station/1890244339129317935">(.+?)for Studying Radio</a>'
pattern = re.compile(regex)

htmlfile = urllib.urlopen(url)
htmltext = htmlfile.read()

titles = re.findall(pattern, htmltext)

# print htmltext
print titles

# fo = open("songlist.txt", "w")
# j = 0
# size = len(titles)
# while j < size:
# 	fo.write(titles[j]+"\n")
# 	song = titles[j]
# 	dict.update({song:1})
# 	print "HH", song
# 	j+=1

# fo.close()
