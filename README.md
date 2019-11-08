# openkv_project
---------------------------------------THIS IS STEP-1--------------------------------------------------------------------
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

-----------------------------------------------THIS IS STEP-2------------------------------------------------------------------
import face_recognition
import cv2
import numpy as np
import pyttsx3
import time
import os
cloc=str(os.getcwd())
def say(word):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(word)
    engine.runAndWait()
    engine.stop()

def project():
    import speech_recognition as sr
    import datetime
    import webbrowser
    from gtts import gTTS
    import time
    import random
    import pyscreenshot as ImageGrab
    import os
    import vlc
    from googletrans import Translator
    import calendar
    import datetime
    import wikipedia
    import mysql.connector as cs
    import pyperclip
    def playaudio(filename):
        p = vlc.MediaPlayer(cloc+str("\\"+filename))
        p.play()
    
    r=sr.Recognizer()
    def note():
        with sr.Microphone() as source:
            print("speak clearly")
            say('speak clearly')
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                hc=1
                print("you said:",text)
        
            except:
                print("sorry nothing heard")
                hc=0

            if hc==1:
                if "dot" in text:
                    text=text.replace("dot",".")
                if "open" in text:
                    if "bracket" in text:
                        text=text.replace("open bracket","(")
                    if "square bracket" in text:
                        text=text.replace("open square bracket","[")
                if "close" in text:
                    if "bracket" in text:
                        text=text.replace("close bracket",")")
                    if "square bracket" in text:
                        text=text.replace("close square bracket","]")
                if "slash" in text:
                    text=text.replace("slash","/")
                if "percent" in text or "percentage" in text:
                    text=text.replace("percent","%")
                if "at the rate" in text:
                    text=text.replace("at the rate","@")
                myfile=open("dictate.txt","w")
                myfile.write(text)
                myfile.close()

    def findfile(cmd):
        exe=0
        for x,d,f in os.walk("c:\\"):
            for files in f:
                if files ==cmd:
                    location=str(os.path.join(x,files))
                    os.startfile(location)
                    exe=1
                    print(location)
        if exe==0:
            print("file not found")
            say("file not found")
          
    def delhistory():
        say("all data is deleted")
        con2=cs.connect(host="localhost",user="root",passwd="",database="catalina")
        cursor2=con2.cursor()
        query2="delete from history;"
        cursor2.execute(query2)
        con2.commit()
        con2.close()

    def speechrecognise():
        with sr.Microphone() as source:
            say('speak clearly')
            print("speak clearly")
            print("sss")
            audio=r.listen(source)
            try:
                text=r.recognize_google(audio)
                if " dot" in text:
                    text=text.replace(" dot",".")
                if "PNG" in text:
                    text=text.replace(" PNG","png")
                if "JPG" in text:
                    text=text.replace(" JPG","jpg")
                if "MP4" in text:
                    text=text.replace(" MP4","mp4")
                if "PDF" in text:
                    text=text.replace(" PDF","pdf")
                if "exe" in text:
                    text=text.replace(" exe","exe")
                if "MP3" in text:
                    text=text.replace(" MP3","mp3")
                if "pptx" in text:
                    text=text.replace(" pptx","pptx")
                if "is equal to" in text and text.isalphanumeric():
                    text=text.replace(" is equal to ","=")
                return (text)
        
            except:
                ch=0
                return ch
    speech=speechrecognise()
    print("you said:",speech)

    def assistant(speech):
        cmd=str(speech)
        delete,p=0,0
        if "note" in cmd:
            print("your voice will be converted to text & will be saved in dictate.txt file")
            time.sleep(5)
            print("start")
            say("start")
            note()
            p=1
        if "what is the time" in cmd or "show me the time" in cmd or "time" in cmd:
            t = time.localtime()
            currenttime = time.strftime("%H:%M", t)
            a=str(currenttime)
            if int(a[:2])>0 and int(a[:2])<12:
                a=a+" AM "
            if int(a[:2])>=12 and int(a[:2])<24:
                h=str(int(a[:2])-12)
                a=h+a[2:]+" PM "
                atext='The time is '+str(a)
                say(atext)
                print(a)
            p=1
        if "set" in cmd and "alarm" in cmd:
            stop = False
            tm=str(input("enter time:"))
            label=str(input("enter label of alarm:"))
            atext='The alarm is set'
            myobj = gTTS(text=atext, lang='en')
            myobj.save("time.mp3")
            a1="time"
            playaudio('time.mp3')
            time.sleep(2)
            c=0
            while stop == False and c!=1:
                rn = str(datetime.datetime.now().time())
                if tm==rn[:8]:
                    print(label,rn[:8])
                    say("wake up wake up wake up wake up wake up wake up wake up wake up wake up wake up wake up wake up ")
                    c,p=1,1
        if "date" in cmd:
            today = datetime.date.today()
            atext='The date is '+str(today)
            say(atext)
            print("Today's date:", today)
            p=1
        if "calendar" in cmd:
            today = datetime.date.today()
            say("calendar of the year is given below")
            y=str(today)
            year=y[0:4]
            print (calendar.calendar(int(year), 2, 1, 6))
            p=1       
        if "who are you" in cmd or "what is your name" in cmd or "your name please" in cmd:
            print("Hello, my name is Catalina.")
            say("Hello, my name is Catalina.")
            p=1
        if "translate" in cmd:
            d={"English":"en","Hindi":"hi","Kannada":"kn","Telugu":"te","Marathi":"mr","French":"fr",
                "Punjabi":"pa","Korean":"ko","Latin":"la","German":"de",'Malayalam':"ml",'Russian':"ru",'Gujarati':"gu"}
            lan="English"
            for i in d:
                if i in cmd:
                    lan=str(i)
                else:
                    a=10
            l=str(d[lan])
            text4=str(input("enter the text to know details:"))
            s = Translator().translate(text=text4, dest=l).text
            atext1=str(s)
            myobj = gTTS(text=atext1, lang=l,slow=False)
            myobj.save("lantranslate.mp3")
            playaudio('lantranslate.mp3')
            print("translated :  ",s)
            p=1
        if "one more" in cmd or "again" in cmd:
            p=1
            con1=cs.connect(host="localhost",user="root",passwd="",database="catalina")
            cursor1=con1.cursor()
            query1="select * from history"
            cursor1.execute(query1)
            dat1=cursor1.fetchall()
            c,count=-1,0
            while count!=6:
                recent=str((dat1[c]))
                if "again" not in recent[44:] or recent[44:] is not "" or "one more" not in recent[44:]:
                    sp=recent[44:]
                    assistant(sp)
                    break
                else:
                    c=c-1
                    count=count+1
            con1.close()
        if "open" in cmd:
            p=1#'''or "Open"''':  
            if "open file" in cmd :
                cmd=cmd[9:]
                cmd=cmd[1:]
                print(cmd)
                print("The file will only be searched in C disk")
                say("searching file in C disk. Wait .")
                findfile(cmd)
            if "" in cmd:
                cmd=cmd.lower()
                print(cmd)
                apps={"chrome":'C:/Program Files/Google/Chrome/Application/chrome.exe',
                      'powerpoint':'C:/Program Files/Microsoft Office/root/Office16/POWERPNT.exe',
                      'settings':'C:/Windows/System32/control.exe',
                      'word':'C:/Program Files/Microsoft Office/root/Office16/WINWORD.exe',
                      'access':'C:/Program Files/Microsoft Office/root/Office16/MSASCCESS.exe',
                      'excel':'C:/Program Files/Microsoft Office/root/Office16/EXCEL.exe',
                      'task manager':'C:/Windows/system32/Taskmgr.exe',
                      'onenote':'C:/Program Files/Microsoft Office/root/Office16/ONENOTE.exe',
                      'command prompt':'C:/Windows/system32/cmd.exe',
                      'onscreen keyboard':'C:/Windows/system32/osk.exe',
                      'notepad':'C:/Windows/system32/notepad.exe',
                      'paint':'C:\Windows\system32\mspaint.exe',
                      'this pc':'C:/'}
                for i in apps:
                    if str(i) in cmd:
                        p=1
                        text3="opening"+str(i)
                        say(text3)
                        os.startfile(apps[i])
            else:
                say("i think software is not installed please install the software and then try again")
                p=1
        if "open YouTube" in cmd or "video of" in cmd:
            if "video of" in cmd or "videos related to" in cmd or "videos" in cmd:
                url="https://www.youtube.com/results?search_query="+cmd
                webbrowser.open(url)
                p=1
        if "history" in cmd:
            if "delete" in cmd :
                delhistory()
                p=1
            else:
                say("fetching your data")
                con1=cs.connect(host="localhost",user="root",passwd="",database="catalina")
                cursor1=con1.cursor()
                query1="select * from history"
                cursor1.execute(query1)
                p=1
                dat1=cursor1.fetchall()
                for i in dat1:
                    print(i)
                con1.close()
        if "os" in cmd or "operating system" in cmd and "my" in cmd:
            import platform
            a=str(platform.platform())
            say(a)
            print(a)
            p=1
        if "show me" in cmd or "" in cmd:
            text3="I found this for you."
            if "images" in cmd or "photos" in cmd:
                r1=cmd
                r1=r1.lstrip("show me images of")
                url="https://www.google.com/search?q="+str(r1)+"&source=lnms&tbm=isch&sa"
                say("i found this ")
                webbrowser.open(url)
                p=1
            if "news" in cmd:
                r1=cmd
                r1=r1.lstrip("show me news of")
                url="https://www.google.com/search?q="+str(r1)+"&tbm=nws&source=lnms&tbm=nws&sa"
                say("i found this ")
                webbrowser.open(url)
                p=1
        if "what can you do" in cmd:   
            say("i can do a lot like managing your activities, play a game, set a remainder,entertain,play a video, and a lot more")
            p=1
        if "copy" in cmd:
            t=cmd[5:]
            pyperclip.copy(t)
            say('text copied')
            p=1
        if "game" in cmd or "play" in cmd:
            if "game" in cmd or "a game" in cmd:
                url1="https://www.google.com/search?q=tic+tac+toe"
                url2="https://www.google.com/search?q=minesweeper"
                url3="https://www.google.com/search?q=play%20snake"
                url4="https://doodlecricket.github.io"
                url5="https://www.bing.com/fun/sudoku"
                url6="https://www.bing.com/fun/chess"
                r5=random.randint(0,5)
                url=[url1,url2,url3,url4,url5,url6]
                url=url[r5]
                say("OK let's play a game")
                print(p)
                p=1
                webbrowser.open(url)
            if "video" in cmd or "music" in cmd or "song" in cmd:
                g=".mp4"
                q=5
                lst=[]
                if 'music' in cmd or "song" in cmd:
                    g=".mp3"
                if q==5:
                    if " " in cmd :
                        say("searching file in c disk")
                        r1=5
                        for x,d,f in os.walk("c:\\"):
                            for files in f:
                                if g in files:
                                    location=str(os.path.join(x,files))
                                    lst.append(location)
                        p=1
                        w=random.randint(0,len(lst)-1)
                        ob=lst[w]
                        print("location:",ob)
                        os.startfile(ob)
        if "image to text" in cmd:
            pr=0
            try:
                from PIL import Image
            except ImportError:
                import Image
            import pytesseract
            import cv2
            file=str(input("enter image name:"))
            if " " in cmd :
                say("searching file in c disk")
                for x,d,f in os.walk("c:\\"):
                    if pr==0:
                        for files in f:
                            if files ==file and pr==0:
                                location=str(os.path.join(x,files))
                                print("location of file------   ",location)
                                img = cv2.imread(location)
                                p,pr=1,1
                                print("____________________________IMAGE PROCESSED TO TEXT________________________________")
                                print(pytesseract.image_to_string(Image.open(location)))
                                project()
                                break
        if "screenshot" in cmd or "take a photo of my screen" in cmd:
            time.sleep(5)
            if __name__ == '__main__':
                im = ImageGrab.grab()
                say("screenshot taken")
                n=str(input("enter name of the file:"))
                im.save(n+'.png')
                p=1
                time.sleep(3)
                im.show()
        if "tell me a joke" in cmd or "make me laugh" in cmd or "make me smile" in cmd or " joke " in cmd:
            j1='''A snail walks into a bar and the barman tells him there's a strict policy about having snails in the bar and so kicks
            him out.A year later the same snail re-enters the bar and asks the barman "What did you do that for?'''
            j2='''Three mice are being chased by a cat. The mice were cornered when one of the mice turned around and barked, "Ruff! Ruff! Ruff!" The surprised cat ran away scared.
            Later when the mice told their mother what happened, she smiled and said, "You see, it pays to be bilingual!"'''
            j3='''A nervous old lady on a bus was made even more nervous by the fact that the driver periodically took his arm out of the window. When she couldn't stand it any longer, she tapped him on the shoulder and whispered on his ear:
            "Young man...you keep both hands on the wheel...I'll tell you when it's raining!"'''
            j4='''Customer: Waiter, waiter! There is a frog in my soup!!! 
            Waiter: Sorry, sir. The fly is on vacation. '''
            j=[j1,j2,j3,j4]
            w1=random.randint(0,3)
            select=j[w1]
            say(select)
            for i in select:
                print(i,end="")
                time.sleep(0.047)
            print()
            p=1
        if "search for" in cmd:
            cmd=cmd.lstrip("search for")
            url="https://www.google.com/search?q="+cmd+"&source"
            say("i found this according to your search")
            p=1
            webbrowser.open(url)
        if "credits" in cmd or "made" in cmd and "you" in cmd:
            say("this is an open source project made by varun, mayank, souranh hope you liked it")
            p=1
        if "features" in cmd or "help" in cmd:
            features=["opening a file/app","entertain","search","weather","calculate","history","game","quiz","puzzle","video",
                    "take screenshot","download video","show time","note","OCR from image","alarm","math problems",'Q and A',"and many more"]
            for i in features:
                say(i)
                print(i)
            p=1
        if "hello" in cmd:
            say('hello, how can I help you')
            p=1
        if "close" in cmd or "turn off"in cmd or "shutdown" in cmd and "computer" in cmd :
            os.system("shutdown -s")
            say("shutting down in  minute")
            p=1
        if "restart" in cmd and"computer" in cmd:
            os.system("shutdown /r /t 1")
            p=1
        if "exit" in cmd or "quit" in cmd or"close" in cmd:
            exit()
            p=1
        if "" in cmd and p==0:
            import wolframalpha
            client = wolframalpha.Client('42XG9Q-L76KJ35T39')
            try:
                res =client.query(cmd)
                output =next(res.results).text
                a=str(output)
                print(output)
                say(a)
                p=1
            except:
                try:
                    if p==0:
                        a=wikipedia.summary(cmd)
                        print(a)
                        say('According to Wikipedia'+a)
                except:
                    link='https://www.google.com/search?q='+str(cmd)
                    webbrowser.open(link)
                    p=1
        if delete!=1:
            con=cs.connect(host="localhost",user="root",passwd="",database="catalina")
            cursor=con.cursor()
            a=datetime.date.today()
            timesave=datetime.datetime.now().time()
            rn = str(timesave)
            tm=rn[:10]
            data=[(str(a),str(tm),cmd)]
            query='insert into history(date,time,word) values(%s,%s,%s)'
            cursor.executemany(query,data)
            con.commit()
            con.close()
            p=1
    if speech==0:
        say("Sorry about that.I didn't hear anything.")
        print("Sorry about that.I didn't hear anything."," :-(")
    else:
        assistant(speech)
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.
# Get a reference to webcam #0 (the default one)

video_capture = cv2.VideoCapture(0)
say("login with your face")
# Load a sample picture and learn how to recognize it.
obama_image = face_recognition.load_image_file(cloc+"\\owner60.png")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Create arrays of known face encodings and their names

known_face_encodings = [
    obama_face_encoding
]
myfile1=open(r'name.txt',"r")
s=myfile1.readlines()
ownername=s[0]+'\n'
myfile2=open(r'loginhistory.txt',"r")
log=myfile2.readlines()
lastuse=log[-1]
known_face_names = [
    ownername,
]
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
count,uc=0,0
while True:
        # Grab a single frame of video
    ret, frame = video_capture.read()
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
        # Only process every other frame of video to save time
    if process_this_frame:
            # Find all the faces and face encodings in the current frame of video

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    # Display the results

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        # Draw a box around the face
        if name=="Unknown":
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0,0 ,255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            uc=uc+1
            if uc==10 and count==0:
                say("unknown face detected")
                winpath = os.environ["windir"]
                os.system(winpath + r'/system32/rundll32 user32.dll, LockWorkStation')
                break
        elif ownername==lastuse:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0,255 ,0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            count=count+1
    # Display the resulting image
    cv2.imshow('ID press Q to exit', frame) # Hit 'q' on the keyboard to quit!
    if count==10:
        say("face detected")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
#_________________________________________________________________________________________________________________________________
while count>9:
    project()
    time.sleep(5)

