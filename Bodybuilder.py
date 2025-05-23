#Creating my QandA dictionary
GritLabFAQ = {
            "hello":" Hey there Gritter! This is Autobot, how are you holding on today ? ",
            "hi":" Hey there Gritter! This is Autobot, how are you holding on today ? ",
            "greetings":" Hey there Gritter! This is Autobot, how are you holding on today ? ",
            "i am doing well":" Wonderful, what do you want to know about Grit Lab? ",
            "fine":" Wonderful, what do you want to know about Grit Lab? ",
            "great":" Wonderful, what do you want to know about Grit Lab? ",
            "what is the meaning of grit?":" Bravery,courage,perseverance and determination despite difficulty",
            "what is grit lab?":" Grit Lab is an accelerated weekly coding programme for students"+
                                 "who are passionate about programming and have demonstrated interest,"+
                                 "evident from the DEV1A module. These students will be exposed to a"+
                                 "wide range of 4IR/technological skills, starting from advanced problem"+
                                 "solving to development of diverse types of software appllications across  "+
                                 "diferrent fields. GRIT students also enjoy career advisory, strong recommendations,"+
                                 "and character mentoring. successful students will go on to become tutors for DEV and"+
                                 "software engineers from their second year till they graduate, working on well-paid real "+
                                 "life projects while acquiring valuable industry experience. In previous years,"+
                                 "GRIT students have recorded  100% employment rate after graduation. Several organisations only hire GRIT students. ",
            "who qualifies for grit lab?":" You need an average of 65% from your DEV1A01 Labs to qualify(Lab Mark,not Final Mark). This is for DEV1 students only,"+
                                          " registered for BCom Information Systems at the University of Johannesburg",
            "what are the rules for the labs?":" Once in,you are in for the entire semester! You miss one week,you are OUT! "+
                                               "You will be dropped if Grit average score is less than 65%, or if you are not performing well in any of your modules.",
            "who is a kingsman academic?":" Is an identity that symbolizes a person that ia able to transcend the divisions in society, cobtinuously acquire future-fit skills, "+
                                          "stay disciplined, apply Grit in their quest for knowledge, solve for society using technology, and help others"
        }

#Proceed = True

global info
info =""
sentence+=""

#while(Proceed):
    
if "quit" in (sentence.lower().split()):
    info+=" Thank you for your time! "
    info+=" For more enquiries, email: abejide@abejide.org " 
    Proceed = False
else:
        
    if "hello" in (sentence.lower().split()) or "hi" in (sentence.lower().split())or "greetings" in (sentence.lower().split()):
        info+=GritLabFAQ["hello"]   
    elif "well" in (sentence.lower().split()) or "fine" in (sentence.lower().split()) or "great" in (sentence.lower().split()):
        info+=GritLabFAQ["fine"]
    elif "meaning" in (sentence.lower().split()):
        info+=GritLabFAQ["what is the meaning of grit?"]
    elif "grit" in (sentence.lower().split()) or "lab" in (sentence.lower().split()):
        info+=GritLabFAQ["what is grit lab?"]
    elif "qualifies" in (sentence.lower().split()):
        info+=GritLabFAQ["who qualifies for grit lab?"]
    elif "rules" in (sentence.lower().split()):
        info+=GritLabFAQ["what are the rules for the labs?"]
    elif "kingsman" in (sentence.lower().split()):
        info+=GritLabFAQ["who is a kingsman academic?"]
        
          