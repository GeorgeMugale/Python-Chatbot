import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import scrolledtext
import time
import urllib.request
from html.parser import HTMLParser
from urllib.error import URLError, HTTPError
import winsound
import time
import os
import turtle




window = tkinter.Tk()
window.title("AUTO")


def widgetDestroyer():
    for widget in window.winfo_children():
        widget.destroy()


window.attributes('-fullscreen',True)

####################    INTRODUCTION WINDOW     ##################################################################

auto = PhotoImage(file = r"AUTO.png").zoom(3, 3)


autoLable = tkinter.Label(window, image=auto, width=500, height=500, bg="orange").pack()
lable1 = tkinter.Label(window, text="AUTO the Chat Bot", bg="orange", font=("Comic Sans",30)).pack()
lable2 = tkinter.Label(window, text="From GRIT Vally", bg="orange", font=("Comic Sans MS Bold",50)).pack()

window.configure(bg="orange")

window.after(2000, widgetDestroyer)




####################    MAIN PROGRAM WINDOW     ##################################################################
class OBJParser(HTMLParser):
    def __init__(self):#constructor
        super().__init__()#chaiining this constructor with constructor of superclass
        self.txt = ""
        self.paragraph = False
        
    def handle_starttag(self, tag, attrs):#these function  members have overloaded versions cause HTMLParser provides methods for handling different parts of an HTML document
        if tag == 'p':
            self.paragraph = True

    def handle_data(self, data):
        if self.paragraph:
            self.txt += data

    def handle_endtag(self, tag):
        if tag == 'p':
            self.paragraph = False

def simplifyParagraph(string):

    char = ""
    pos = 0
    count = 0
    for i in range(len(string)) :
        pos+=1
        if string[i] == ".":
            count+=1
        if count == 4 :
            break

    return string[0:pos]

def lineController(string):

    shortLine = ""
    paragraph = ""

    if len(string)>2:

        for word in string.split():
            if len(shortLine + word) < 50:
                shortLine += word + " "
            else:
                paragraph += shortLine + "\n"
                shortLine = word + " "
    

    return paragraph


def widgetCreator():
    global advanced
    advanced = False
    global info
    info = ""

    def speechBubbler(string):
        label = tkinter.Label( chatWindow, text=string, background="orange", font = ("Arial Narrow OS", 15), anchor="w", justify="left")#bind lable to scrolled text
        return label

    def speechBubbler2(string):
        label = tkinter.Label( chatWindow, text=string, background="light goldenrod", font = ("Arial Narrow OS", 15), anchor="w", justify="left")#bind lable to scrolled text
        return label

    def answerAUTO(string):
        chatWindow.insert(tkinter.END, '\n', 'left')
        chatWindow.window_create(tkinter.END, window=speechBubbler(string))
        chatWindow.insert(tkinter.END, "\n" + "\n", "left")
    

    def Reply():
      
        chatWindow.tag_configure("left", justify="left")
        chatWindow.tag_configure("center", justify="center")
        chatWindow.tag_configure("right", justify="right")

        userInput = ""
        userInput = chatBox.get("1.0", tkinter.END)

        chatWindow.configure(state="normal")

        if (len(userInput)<=2):
            chatBox.delete("1.0","end")
            chatWindow.insert(tkinter.END, '\n ', 'right')
            chatWindow.window_create(tkinter.END, window=speechBubbler2("    "))
            chatWindow.insert(tkinter.END, '\n '+ '\n ', 'left')
            answerAUTO("I'm sorry I don't think that's a question")

        else:
            ##if auto knows answer
            chatBox.delete("1.0","end")
            chatWindow.tag_configure("left", justify="left")
            chatWindow.tag_configure("center", justify="center")
            chatWindow.tag_configure("right", justify="right")

            chatWindow.insert(tkinter.END, '\n ', 'right')
            chatWindow.window_create(tkinter.END, window=speechBubbler2(userInput))

            path = []
            path = ["Bodybuilder.py","sunMoonUJ.py", "GRITVALLEY-FRACTALPART\CHATEBOT_FRAC.py"]
           
            
            sentence=userInput

            global info
            try:
             
                for i in path:
                    file = open(i,"r")  
                    code = file.read()
                
                    exec(code)                 
                    file.close()
            except:
                info+="I'm sorry, something went wrong"

            
            global advanced
            if len(info)!=0:##if auto knows answer
                info=lineController(info)
                answerAUTO(info)

            if len(info)==0 and advanced==True:##if auto does not know and advanced setting is on

                try:
                    query = urllib.parse.quote(userInput)
                    search = f"https://en.wikipedia.org/w/index.php?search={query}"
            
                    # websites may block or restrict requests that do not have a valid User-Agent header.
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'} #Dictionary that contains a common example of an HTTP User-Agent header.
                    try:
                        #the User-Agent header is part of the HTTP request sent by a web client
                        request = urllib.request.Request(search, headers=headers)

                        with urllib.request.urlopen(request) as pageResult:

                            rawHTMLContent = pageResult.read()
                            pageResult.close()
                        
                            charset = pageResult.headers.get_content_charset() 

                            if charset is None:
                                charset = 'utf-8'

                            strHTML = rawHTMLContent.decode(charset)#decoding html with correct character set

                            parser = OBJParser()
                            parser.feed(strHTML)
   
                            info = lineController(simplifyParagraph(parser.txt))

                    except Exception as e:
                        #handle other errors
                        info = "Opps! There is an issue, the page could not load."

                    except HTTPError as e:
                        # Handle HTTP errors
                        info = "I am sorry, the HTTP request indicated an error. HTTP Error: {e.code} - {e.reason}"
                    except URLError as e:
                        # Handel URL errors
                        info = "I am sorry, the page could not seem to load due to URL-related errors, such as network issues or invalid URLs." 
                    except TimeoutError as e:
                        # Handle TimeoutError
                        info = "servers did not respond due to slow connection or server being down"
                
                    except request.exceptions.RequestException as e:
                         #handle other errors
                         info = "Opps! There is an issue, the page could not load."

                    except:
                        info = "Opps! There is an issue, the page could not load."

                    if len(info)==0:
                        info = "I am sorry, the search was not specific enough."

            
                except:
                     info = "Opps! There is an issue, the page could not load."

                answerAUTO("I was unable to find the answer in my libraries \n heres a wiki i complied that might be of some use")
                answerAUTO(info)

            elif len(info)==0:
                answerAUTO("I'm sorry I dont know.") 

                
        chatWindow.configure(state="disabled")
        chatWindow.see(END)
        

    def LightMode():
        chatWindow.configure(bg="goldenrod", fg="black")
        chatBox.configure(bg="goldenrod", fg="black")
        radD.configure(fg="black", bg="khaki2")
        radL.configure(fg="black", bg="khaki2")
        window.configure(bg="khaki2")
        baseFrame.configure(bg="khaki2")
        chatFrame.configure(bg="khaki2")
        lbl.configure(fg="black", bg="khaki2")
        chkA.configure(fg="black", bg="khaki2")


    def DarkMode():
        chatWindow.configure(bg="grey14", fg="khaki2")
        chatBox.configure(bg="grey14", fg="khaki2")
        radD.configure(fg="orange", bg="black")
        radL.configure(fg="orange", bg="black")
        lbl.configure(fg="goldenrod", bg="black")
        window.configure(bg="black")
        baseFrame.configure(bg="black")
        chatFrame.configure(bg="black")
        chkA.configure(bg="black", fg="orange")
     
    def changeMode():
        global advanced
        advanced= not(advanced) 

    window.configure(bg="khaki2")
    baseFrame = Frame(window, bd = 5, height = 70, bg="khaki2")
    chatFrame = Frame(window, bd = 5, height = 60, bg="khaki2")

    btnSend = tkinter.Button(chatFrame,  height = 60, width = 60, image=photo, bg="darkgoldenrod4", font = ("Arial Narrow OS", 15), cursor="hand2", command=Reply)
    btnSend.pack(side="right")
    chatBox = scrolledtext.ScrolledText(chatFrame , width=200, height=2, bd=10, font = ("Arial Narrow OS", 15), bg="goldenrod") 
    chatBox.pack(side="left")
    chatBox.focus()

    chatWindow = scrolledtext.ScrolledText(window, width=200, bd=10,font = ("Arial Narrow OS", 15), bg="goldenrod",  state="disabled", cursor="hand2")
    
    chatWindow.pack(fill="y")
    chatWindow.focus()

    checkVar = tkinter.BooleanVar()
    radD = Radiobutton(baseFrame,text="Dark Mode", value=2, command=DarkMode, font = ("Arial Narrow OS", 12), bg="khaki2")
    radL = Radiobutton(baseFrame,text="Light Mode", value=1, command=LightMode, font = ("Arial Narrow OS", 12), bg="khaki2")
    chkA = Checkbutton(baseFrame, text="Advanced", variable=checkVar, command=changeMode, font = ("Arial Narrow OS", 12), bg="khaki2")

    lbl = Label(baseFrame, text="A GRIT Vally Production", font = ("Arial Narrow OS", 20), bg="khaki2")

    radL.grid(column=0, row=0)
    radD.grid(column=1, row=0)
    lbl.grid(column=2, row=0, padx=310)

    chkA.grid(column=3, row=0, padx=100)
 

    baseFrame.pack(side="bottom", fill="x", ipady=0)
    chatFrame.pack(side="bottom", fill="x", ipady=0)
    baseFrame.configure(bg="khaki2")
    chatFrame.configure(bg="khaki2")

window.after(2001, widgetCreator)

photo = PhotoImage(file = r"send.png").zoom(2, 2)   
UJFlag = PhotoImage(file = r"UJ-PicFlag.png").zoom(1, 1)  
UJSport = PhotoImage(file = r"UJ-PicSport.png").zoom(1, 1)   
Sun = PhotoImage(file = r"SUN-Pic.png").subsample(2, 2)  
Moon = PhotoImage(file = r"MOON-Pic.png").subsample(3, 3) 

GL_UNKNWON =  PhotoImage(file = r"JBS FRACTALS\GL-UNKNOWN.png").subsample(3,3)
JBS_GL027 = PhotoImage(file = r"JBS FRACTALS\JBS-GL027.png").subsample(3,3)
JBS_GL033 = PhotoImage(file = r"JBS FRACTALS\JBS-GL033.png").subsample(3,3)
JBS_GL116 = PhotoImage(file = r"JBS FRACTALS\JBS-GL116.png").subsample(2,2)
JBS_GL292 = PhotoImage(file = r"JBS FRACTALS\JBS-GL292.png").subsample(2,2)
JBS_GL295 = PhotoImage(file = r"JBS FRACTALS\JBS-GL295.png").subsample(2,2)
JBS_GL305 = PhotoImage(file = r"JBS FRACTALS\JBS-GL305.png").subsample(2,2)
JBS_GL310 = PhotoImage(file = r"JBS FRACTALS\JBS-GL310.png").subsample(1,1)
JBS_GL342 = PhotoImage(file = r"JBS FRACTALS\JBS-GL342.png").subsample(2,2)
JBS_GL385 = PhotoImage(file = r"JBS FRACTALS\JBS-GL385.png").subsample(2,2)
JBS_GL464 = PhotoImage(file = r"JBS FRACTALS\JBS-GL464.png").subsample(2,2)

global fracts
fracts = {}
fracts["1"]=GL_UNKNWON
fracts["2"]=JBS_GL027
fracts["3"]=JBS_GL033
fracts["4"]=JBS_GL116
fracts["5"]=JBS_GL292
fracts["6"]=JBS_GL305
fracts["7"]=JBS_GL310
fracts["8"]=JBS_GL342
fracts["9"]=JBS_GL385
fracts["10"]=JBS_GL464


global pics
pics = {}
pics["key"] = "picture"
pics["key2"] = "pic"
pics["key3"] = "show"
pics["uj"] = UJFlag
pics["flag"] = UJFlag
pics["Sport"] = UJSport
pics["team"] = UJFlag
pics["sun"] = Sun
pics["moon"] = Moon


window.mainloop()


