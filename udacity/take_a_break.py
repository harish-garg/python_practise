import time
import webbrowser

count = 1
while (count <= 3):
    time.sleep(10)
    webbrowser.open("http://www.google.com")
    count += 1


