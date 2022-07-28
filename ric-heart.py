from flask import Flask, render_template, request
from googlesearch import search
import os


app = Flask(__name__)

#Storage of User Inputs might have to change later the input to a file needs to be where algo can repeatedly add onto to use inputs later to 
#search recipes


Input = [] #client input 
Ques = ["Panckes or waffles?", "What fruit would you want?", "Would you want a cake or cupcakes?",  "What spices do you want to use?", "Do you want the dish cold or hot?", "Would you like soup or sandwhich" ]# [ "What meat do you want in your dish?", "Do you want a sandwich-like dish? (Sausage biscuit, bagel sandwich)", "What spices do you want to use?"



#fixes wording for allergy food or unwanted ingredients
#Setup for search
#Allergy:   input-free
#Unwanted:  -input
def checker(x):
    #splits the client inputs
    ch = x.split()

    #Allergies
    for i in ch:
        if  i == "gluten" or i == "shellfish" or i == "peanut" or i == "dairy":
            Input.append(i + "-free")
        #Uwanted Ingredients
        else:
            Input.append("-" + i)
    #picks up the next question in the bank     
    nextQues = Ques[0]
    Ques.pop(0) #getting rid of question so it is not reused again 
    return nextQues
    


def interact(userText):

    if len(Ques) == 0 or userText == "results":
        botResponse = results()
    elif userText == "":
        #obtaining the next question in the bank and removing it since used 
        botResponse = Ques[0]
        Ques.pop(0)
    elif userText == "yes":
            userText.partition[-1] #gets the last word in the list which is the keyword?
            keyword = userText.substring(0, userText.length() - 1)# getting rid of ? from keyword
            Input.append(keyword)#adding to list
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
    r = search(query, tld="co.in", num=1, stop=1)
    return r
    

#first page
@app.route("/")
def index():
    return render_template("index.html")

#the second page where the chat box is 
@app.route("/chat")
def home(): 
	return render_template("home.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg') #intakes the use input 
    #used for the inital start of the chatbox checking if their is no current inputs saved
    if len(Input) == 0:
        botResponse = checker(userText)
    else:
        botResponse = interact(userText)

    return botResponse
    
app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
