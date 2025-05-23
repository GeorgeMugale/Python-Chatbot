import random

def wordfinder(sentence, word):
        if (sentence.find(word) == -1): 
            return "NO" 
        else:
            return "YES"

keyword1={}
keyword1["key"]="moon"

keyword1["when"]="The moon, discovered in 1609, is 4.5 billion years old and has been the subject of significant discoveries by scientists over the 360-year period between Galileo's observations and Apollo 11 landing."
keyword1["what"]="The Moon's phases refer to the various shapes it appears in different times of the month, from a large sphere to a narrow crescent, bright circle, or even invisibility."
keyword1["where"]="The Moon is Earth's only natural satellite. It orbits at an average distance of 384400 km (238900 mi)."

keyword1["who"]="Thomas Harriot, an English astronomer, made the first recorded observations of the Moon in July 1609, a month before Galileo."
keyword1["how"]="The moon, formed during a collision between Earth and Mars, orbits Earth once every 27.322 days in an elliptical circle, with a diameter of 2,159 miles. It is tidally locked with Earth and illuminated by sun light."
keyword2={}
keyword2["key"]="sun"
keyword2["when"]="The sun, created 10 billion years ago, will eventually die due to hydrogen running out, which should not occur for 5 billion years, followed by star death phases 2-3 billion years later."
keyword2["what"]="The sun is an ordinary star, one of about 100 billion in our galaxy, the Milky Way. The sun has extremely important influences on our planet."

keyword2["how"]="The Sun, a dense gas, generates energy through nuclear fusion reactions, creating helium from hydrogen. Earth's orbit around the Sun is 864,400 miles."
keyword2["who"]="Galileo Galilei, an Italian astronomer born in 1564, made significant contributions to our understanding of our place in the Universe through his observations of the solar system and the Milky Way."
keyword2["where"]="at the center of our solar system. It's about 93 million miles (150 million kilometers) from Earth and it's our solar system's only star."




keyword3={}
keyword3["key"]="uj"
keyword3["when"]="On 1 January 2005, the University of Johannesburg came into being after two years of negotiations."

keyword3["what"]="UJ is a public university in South Africa, known for its world-class academic programs and international recognition. It prepares students for work and global citizenship. The university's logo features two birds representing the union of two respected institutions, symbolizing freedom and the University of Johannesburg Hoopoe."
keyword3["where"]="UJ has four campuses in Johannesburg's metropolitan area: Auckland Park Kingsway, Auckland Park Bunting Road, Doornfontein, and Soweto."
keyword3["apb"]="UJ Auckland Park Bunting is the largest campus in Auckland Park, located near the Faculty of Arts, Design and Architecture, offering banking services and various food outlets."
keyword3["auckland park"]="UJ Auckland Park Bunting is the largest campus in Auckland Park, located on Bunting road. It is situated next to the Faculty of Arts, Design and Architecture building and offers multiple banking services from major South African banks, as well as fast and traditional food outlets."
keyword3["apk"]="UJ Auckland Park Kingway is the largest campus located on Kingway Ave, with the largest center featuring outlets like Postnet, Fundi, Van Schaik, and other fast-food outlets."
keyword3["dfc"]="UJ Doornfontein Campus, situated on 25 Louisa Street in Johannesburg, features a gymnasium, food and electronics outlets, and a variety of other facilities."
keyword3["Doornfontein"]="The center, situated on 25 Louisa Street in Doornfontein Johannesburg, features a gymnasium at the entrance, along with various food and electronics outlets."
keyword3["soweto"]="The UJ Law campus, located in Soweto, Johannesburg, was formed in 1809 through a merger of Rand Afrikaans University, Technikon Witwatersrand, and Vista University's Soweto and East Rand campuses."
keyword3["swc"]="UJ Soweto campus, now UJ Law, is a Johannesburg 1809 merger of Rand Afrikaans University, Technikon Witwatersrand, and Vista University's Soweto and East Rand campuses."
keyword3["apply"] = "Applications for 2024 open on 1 April and the closing date for applications is 31 October 2023 at 12:00. \n The link to apply is: \n https://www.uj.ac.za/faculties/art-design-and-architecture/departments-2/interior-design/apply-now/"

keyword3["courses"] = "UJ offers courses such as \n Post graduate Diploma in Business Management \n Continuing Education Programme \n B Com Honours Strategic Management \n M Com Business Management – Coursework & Dissertation \n BSc Information Technology \n BSc Computer Science and Informatics and many more"

keyword3["campus"]="APK and APB are located in Auckland Park, DFC in Doornfontein, and SWC in Soweto Johannesburg."

keyword3["how"]= "The University of Johannesburg, formed in 2005, requires a minimum 27 APS scores and a 60%+ English proficiency, covering over 600,000 square meters."
keyword3["who"]="Professor Letlhokwa George Mpedi, the newly appointed Vice-Chancellor and Principal of the University of Johannesburg, was officially inaugurated on 10 March 2023."
keyword3["about"]= "The University of Johannesburg (UJ) is a multicultural institution with seven faculties, a college, and four campuses, offering education, law, humanities, art, design, architecture, and health sciences. With over 50,000 students, UJ aims for excellence in research, innovation, teaching, international profile, student-friendly living experience, and reputation management."
keyword3["fact"]=keyword3["about"]


keyword4={}
keyword4["key"]="university of johannesburg"
keyword4["when"] = keyword3["when"]
keyword4["who"] = keyword3["who"]
keyword4["where"] = keyword3["where"]
keyword4["how"] = keyword3["how"]
keyword4["apk"] = keyword3["apk"]
keyword4["apb"] = keyword3["apb"]
keyword4["swc"] = keyword3["swc"]
keyword4["soweto"] = keyword3["soweto"]
keyword4["auckland park"] = keyword3["auckland park"]
keyword4["Doornfontein"] = keyword3["Doornfontein"]
keyword4["apply"] = keyword3["apply"]
keyword4["courses"] = keyword3["courses"]
keyword4["what"] = keyword3["what"]
keyword4["dfc"] = keyword3["dfc"]
keyword4["campus"] = keyword3["campus"]
keyword4["about"] =keyword3["about"]
keyword4["fact"] =keyword3["fact"]


list1=[keyword1,keyword2, keyword3, keyword4]#.....more key words dictionaries

sentence+=""
listt=list(list1)

global info
info += ""
reply=""
for item in listt:
    if wordfinder(sentence.lower(), item["key"].lower())=="YES":
        count = 0
        for j in item:    
                if wordfinder(sentence.lower(),j.lower())=="YES" and j!="key": 
                    reply += item[j]
                    count += 1
        if  count==0 and j!="key":
            for j in item:    
                reply += item[j]
count = 0            
if wordfinder(sentence.lower(), pics["key"].lower())=="YES" or wordfinder(sentence.lower(), pics["key2"].lower())=="YES" or wordfinder(sentence.lower(), pics["key3"].lower())=="YES":
    for j in pics:    
        if wordfinder(sentence.lower(),j.lower())=="YES" and j!="key" and j!="key2" and j!="fractal": 
            chatWindow.insert(tkinter.END, '\n', 'left')
            chatWindow.image_create(tkinter.END, image=pics[j])
            if count ==0:
                info = "here is the picture. \n" + info
                count +=1
                
if "fractal" in sentence.lower():
    chatWindow.insert(tkinter.END, '\n', 'left')
    chatWindow.image_create(tkinter.END, image=fracts[str(random.randint(1, 10))])
    info = "here is the fractal picture. \n" + info       
        

if "draw" in sentence.lower().split():
    answerAUTO("Done! check turtle window")
    
elif "clear" in sentence.lower().split():
    answerAUTO("Page has been refreshed.")

info += reply