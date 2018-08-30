import time
import webbrowser

i = 0

print("this program started on " + time.ctime())

while i <= 2:
    time.sleep(2)
    webbrowser.open("http://www.baidu.com")
    i = i + 1

print("this program ended at " + time.ctime())
