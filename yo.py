import webbrowser 
import time 
import os 

inpt = 'https://www.youtube.com/watch?v=LdjRqgF_z9w'
inpt2 = 5 
inpt3 = 'firefox' 

def OpenUrl(): 
 print ("Viewed.") 
 os.system("TASKKILL /F /IM " + inpt3 + ".exe") 
 webbrowser.open(inpt) 
 time.sleep(int(inpt2)) 
 OpenUrl()