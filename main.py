import pytube
url = input("url gir ")
path =""
# boş verirsek main.py nerdeyse oraya kaydeter.
pytube.YouTube(url).streams.get_highest_resolution().download(path)

