import cv2
import pyttsx3
import mysql.connector as cs
def say(word):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(word)
    engine.runAndWait()
    engine.stop()

camera = cv2.VideoCapture(0)
for i in range(61):

    return_value, image = camera.read()
    if i==60:
        cv2.imwrite('owner'+str(i)+'.png', image)
del(camera)
say("enter your name")
n=str(input("enter your name:"))
say("enter passward of mysql")
passwd1=str(input("enter passward of mysql:"))
myfile1=open(r'name.txt','w')
myfile1.write(n)
myfile1.close()
myfile2=open('loginhistory.txt',"a")
n=n+'\n'
myfile2.write(n)
myfile2.close()
say("face data saved")

con=cs.connect(host="localhost",user="root",passwd=passwd1)
cursor=con.cursor()
try:
    cursor.execute("create database catalina")
    cursor.execute("use catalina")
    cursor.execute("create table history (date date,time varchar(15),word varchar(2048));")

    con.commit()

except:
    say("table exists")
    print("table exist")
    
