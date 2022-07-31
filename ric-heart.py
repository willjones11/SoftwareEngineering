#libraries needed for the app
from flask import Flask, render_template, request
import flask
from googlesearch import search
import os

app = Flask(__name__, template_folder='templates', static_folder='templates/static')

Input = [] #user input 
#Question bank for RIC-BOT
Ques = []




#fixes wording for allergy food or unwanted ingredients
#Setup for the first question RIC-BOT states on startup
#Allergy:   input-free
#Unwanted:  -input
def checker(x):
   
    #if the user doesnt want the question posed it seeks next question
    if x == "no" or x == "none":
        #so next question answer will not run through checker()
        Input.append(" ")
        #obtaining the next question in the bank and removing it since used 
        botResponse = Ques[0]
        Ques.pop(0)
        return botResponse

    #splits the user inputs
    ch = x.split()

    #checking all user inputs 
    for i in ch:
        
        #if the user has allergies applying the correct 
        if  i == "gluten" or i == "shellfish" or i == "nut" or i == "dairy":
            Input.append(i + "-free")
        
        #Uwanted Ingredients
        else:
            Input.append("-" + i)

    #picks up the next question in the bank     
    nextQues = Ques[0]
    Ques.pop(0) #getting rid of question so it is not reused again 
    return nextQues 
    

#main part of checking the user input and taking in inputs for the questions
def interact(userText):

    #if the user wants the results of the questionaire
    if len(Ques) == 0 or userText == "results":
        botResponse = results()

    #if the user doesnt want the question posed it seeks next question
    elif userText == "no" or userText == "none":
        #obtaining the next question in the bank and removing it since used 
        botResponse = Ques[0]
        Ques.pop(0)
    
    #if the user wants the keyword that is asked in the question 
    elif userText == "yes":
        userText[:-1] #gets rid of the ? at end
        keyword = userText.split() #seperates words out to get keyword at end
        Input.append(keyword[-1])#adding to list
        botResponse = Ques[0] #next question for ricbot
        Ques.pop(0) #deletes used question
    
    #for questions with open ended responses usually allows for more keywords to be taken in than yes/no questions 
    else:

        #taking in user input and storing in list
        x = userText.split(" ")

        for word in x:
            Input.append(word)
        
        #obtaining the next question in the bank and removing it since used 
        botResponse = Ques[0]
        Ques.pop(0)

    return botResponse
        
    
#gives the user the result to the questions posed by RIC-BOT
def results():

    #Convert list to String
    query = ' '.join(Input) + ' recipe'
    #print out the google search result
    r = search(query, num=1, stop=1, pause=1)#trys to extract first result
    ans = "Here is your result! Copy and paste the link to view: " + str(list(r)[0])

    return ans
    

#loads the Launch page
@app.route("/")
def index():
    return render_template("index.html")

#loads Chat box hosted second page. This is done when  button is pressed on the launch page
@app.route("/chat")
def home(): 
    Input.clear() #making sure no user inputs from previous state
    Ques.clear() #making sure no left over questions from previous state
    Ques.extend([
    "Pancakes or waffles?",
    "What fruit would you want?",
    "What meat would you like?",  
    "In the dish, do you want sugar?",
    "Do you want the dish to be keto?", 
    "What vegetables would you like?", 
    "Do you want a sandwhich?", 
    "Do you want soup?",  
    "Do you want the dish to be cold or hot?", 
    "What type of cusine would you like? ex. Tex-Mex, Asian or type no for no preference", 
    "Do you want your meal to be organic", 
    "What type of oil would you like to use in the dish? answer as typeoil where type is the oil you want", 
    "Would you want this made in the oven, microwave, stove, grill , crock-pot, or air-fryer", 
    "Would you want your meal to be mild, spicy, or bland", 
    "Would you want the dish to be sweet or savory"
    ])
    return render_template("ric-bot.html")


#Function for interaction between javascript in ric-bot.html and other functions in the python code
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg') #intakes the use input 
    #cleaning input
    userText = userText.lower()

    #used for the inital start of the chatbox checking if their is no current inputs saved
    if len(Input) == 0:
        botResponse = checker(userText)
    #if the user wants the results of the questionaire
    elif len(Ques) == 0 or userText == "results":
        botResponse = results()

    elif userText == "results":
        flask.redirect(flask.url_for("home"))

    #for most quesitons open ended and yes/no
    else:
        botResponse = interact(userText)

    return botResponse 

#helping the app run for flask     
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
