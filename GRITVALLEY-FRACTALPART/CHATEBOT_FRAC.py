#importing time library to delay printing


#sentence = "draw a square"
#global info
#info = ""
#info +=""
sentence+=""         


#getting the response
def GetResponse(a):
    g = open("GRITVALLEY-FRACTALPART\Response.txt","r")
    Speak = False
    phrase = ""
    for line1 in g:
        
        if ("EOF" in line1):
            Speak = False
            break
        if Speak:
            phrase = phrase + line1
        if (a in line1):
            Speak = True
    global info      
    g.close()
    global info
    info+=phrase
    return

#getting code to execute
def GetCode(a):
    g = open("GRITVALLEY-FRACTALPART\Executions.txt","r")
    T = open("GRITVALLEY-FRACTALPART\Tempfile.txt","w")
    Speak = False
    for line1 in g:
        if("EOF" in line1):
            Speak = False
        if Speak:
            T.write(line1 + "\n")
        if(a in line1):
            Speak = True
            
    T.close()
    g.close()
    f = open("GRITVALLEY-FRACTALPART\Tempfile.txt","r")
    exec(f.read())
    

#draw words
def DWord(a):
    c = open("GRITVALLEY-FRACTALPART\Alphabets.txt","r")
    d = open("GRITVALLEY-FRACTALPART\Tempfile.txt","w")
    Speak = False
    for line1 in c:
        if ("EOF" in line1):
            Speak = False
        if Speak:
            d.write(line1 + "\n")
        if((a.upper() + "^") in line1):
            Speak = True
    d.close()
    c.close()
    e = open("GRITVALLEY-FRACTALPART\Tempfile.txt","r")
    exec(e.read())
        
        
    
#checking if the request contains any keywords
Temp_word = ""
#Getting the  user input and making it all caps
#checking if the user wants to stop

Request = sentence.upper().split()

#dictionary to search weather bot should speak or code
SPEAK = False
DRAW = False

Que_dict = {"SPEAK" : ["WHAT", "HOW", "WHEN","WHO","WHERE"], "CODE" : "DRAW"}
Key_list = ["TURTLE","SQUARE","CIRCLE","TRIANGLE","RECTANGLE","ANIMATION","FRACTAL"]

    
for word in Request:
    if word in Que_dict["SPEAK"]:
        SPEAK = True
        if DRAW:
            SPEAK = False           
        Temp_word += word
    elif word in Que_dict["CODE"]:
        DRAW = True
        if SPEAK:
            DRAW = False
        Temp_word +=word
    if word in Key_list:
        Temp_word += word
        
#if the request has any keywords respond accordingly
if ("CLEAR" in sentence.upper()):
    turtle.reset()
    print(sentence)
    global info
if (Temp_word == ""):
    info+=""
elif(Temp_word == Key_list[0]):
    info+="User wants me to draw a turtle"
elif(Temp_word == "DRAW"):
    count = 0
    place = -100
    for word in Request:
        if word == "DRAW":
            count = 0
        else:
            for char in word:
                turtle.up()
                turtle.goto(place + count, 50)
                turtle.down()
                DWord(char)
                count = count + 200
    info+="Done! check turtle window"
        
else:# get response from the file
    if SPEAK: 
        GetResponse(Temp_word)
    if DRAW:
        GetCode(Temp_word)
        info+="Done! check turtle window"
        os.remove("GRITVALLEY-FRACTALPART\Tempfile.txt")
            
            
                 
    

