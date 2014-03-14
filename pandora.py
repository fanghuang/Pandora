import urllib
import re

# symbolfile = open(".txt")
# url = symbolfile.read()

i = 0
fo = open("songlist.txt", "w")
while i < 20:
	
# url = "http://www.pandora.com/profile/stations/billgeorge1"
	if i < 2:
		url = "http://www.pandora.com/content/station_track_thumbs?stationId=1026742826420861487&page=true&posFeedbackStartIndex="+str(5*i)
	else:
		url = "http://www.pandora.com/content/station_track_thumbs?stationId=1026742826420861487&page=true&posFeedbackStartIndex="+str(10*(i-1))

	regex = '<h3><a href=[^.]*>(.+?)</a> by'
	pattern = re.compile(regex)

	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()

	titles = re.findall(pattern, htmltext)
	# str1 = ''.join(titles)
	# print titles
	# playlist.append(titles)
	i+=1


	
	j = 0
	size = len(titles)
	while j < size:
		fo.write(titles[j]+"\n")
		song = titles[j]
		dict.update({song:1})
		print "HH", song
		j+=1

fo.close()
