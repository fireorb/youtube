import webbrowser
import time
import os

print '\t\t\t ######################################'
print '\t\t\t ##                                  ##'
print '\t\t\t ##   Author : Sandeep Saini         ##'
print '\t\t\t ######################################'




url = 'https://www.youtube.com/watch?v=LdjRqgF_z9w'
refresh = 5
brow = 'firefox'

def OpenUrl():
	print("Successfully Viwed. ")
	os.system(" killall -9 " + brow)
	webbrowser.open(url)
	os.system("sh ipchange")
	time.sleep(int(refresh))

for i in range(100):
	OpenUrl()