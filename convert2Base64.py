import base64
import requests

response = requests.get("http://images.indianexpress.com/2016/03/google-doodle-holi_7591.jpg")
uri = ("data:" + 
               response.headers['Content-Type'] + ";" +
                      "base64," + str(base64.b64encode(response.content).decode("utf-8")))
print uri
