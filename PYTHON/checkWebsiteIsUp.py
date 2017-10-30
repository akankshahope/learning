import urllib
import sys
#We can try to get the url from the user and make this dynamic script
try:
    httpcode =  urllib.urlopen("http://www.google.com").getcode()
    if httpcode == 200:
        print "Site is up and running"
    else:
        print "Site is not up"
except:
    print "Oops!  Exception occured for this site: ", sys.exc_info()[0]
