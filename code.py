import ctypes
import requests


url = "https://api.unsplash.com/photos/?client_id="
url1 = "https://source.unsplash.com/random/1980x1080"
key = "ee3fbc4ddce2ba7128e014268b4d5344937a1c78cbea0e574cf4e85e0a4daa36"
response = requests.get(url1)
f = open('image.jpg', "wb")
f.write(response.content)
f.close()
ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\PyCharm Projects\Api_projects\image.jpg", 0)
