import base64
import requests
url = "http://images.freeimages.com/images/previews/118/bicycle-sign-3-1442216.jpg"
response = requests.get(url)
convertedData = ("data:" + 
               response.headers['Content-Type'] + ";" +
                      "base64," + str(base64.b64encode(response.content).decode("utf-8")))
print convertedData
