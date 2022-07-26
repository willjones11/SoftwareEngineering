#Algorithm start by outside call prob the start button 
# have a way to where the user input starts the search of the results maybe from google
#have a way where the inputs are stored and are ready to search when answer is wanted 
#Types of Questions to ask:
    #What types of Cuisine do you not like?   -input
    #Any allegries?    input-free
    #Dessert or dinner? "sweet" "savory".            #needs to be at front to determine the next set of questions
    #What Spices do you want to use? input parsed
    #Do you want vegtables? vegtables -vegtables
    #Do you want fruit? fruit -fruit 
    #Are you wanting a certian cusine? input
    #Do you want soup? soup -soup
    #Would you like a sandwich? sandwich -sandwich
    

#### TO DO and POSSIBLE THOUGHTS
#
#. maybe create the Input to where it outputs the user responses at the end to make changes or confirm before answer is submitted 
#
#  on name input check for profanities
#  
#
#
#importing packages to setup flask and app
from flask import Flask, request, render_template
from flask_socketio import SocketIO, emit 
from googlesearch import search
app = Flask(__name__)
socketio = SocketIO(app)


#Storage of User Inputs might have to change later the input to a file needs to be where algo can repeatedly add onto to use inputs later to 
#search recipes
def _init_(self, name, Input):
    self.name = None
    self.Input = [] #client input 
    self.Ques = [["Panckes or waffles?", "What fruit would you want?", "Would you want a cake or cupcakes?",  "What spices do you want to use?", "Do you want the dish cold or hot?"  ], [ "What meat do you want in your dish?", "Do you want a sandwich-like dish? (Sausage biscuit, bagel sandwich)", "What spices do you want to use?",
     "Do you want vegetables?", "Do you want your dish cold or hot?"]] #[0]= sweet [1]=savory
#starting the chatbox
@app.route('/', methods=['GET"'])
def startup():
    return render_template('index.html') #after pressing button to start chatbox it loads the html page of the chatbox

#start of the interaction 
@app.route('/introduce', methods=['GET', 'POST'])
def start(self):
    print("Hello My Name is RIC-BOT, lets find you a recipe today!") #greeting
    self.name = input("What is your name? ") #intakes the clients name
    #self.name  = request.args.get('username')
    #self.Input = request.args.get('choice')
    print("Hello,  ",  self.name ) #responds 
    ans = input("Are we looking for Breakfast, Lunch, Dinner, or Dessert?") #interaction to start what type of meal client is looking for 
    self.Input.append(ans)# adds answer to list of client inputs
    interact() #calls interact function to begin conversation 

@app.route('/', methods=['GET', 'POST'])
def interact(self):
    #checks for allergies 
    print("Any food allegries or food to avoid")
    x = input()
    checker(x) #calls function to check answer
    ans = input("Do you want sweet or savory meal?")
    self.Input.append(ans)
    if ans == "savory":
        for i in range(0, len(self.Ques[1][1:])):
            print(self.Ques[1][i])
            an = input()
            #if user wants to see their food answer from ric-bot
            if an == "result":
                break
            elif an == "none":
                continue
            self.Input.extend(an)

        
    if ans == "sweet":
        for i in range(0, len(self.Ques[0][1:])):
            print(self.Ques[0][i])
            an = input()
            #if user wants to see their food answer from ric-bot
            if an == "result":
                break
            if an == "none":
                continue
            an = an.split()
            self.Input.extend(an)
    
    end()


#fixes wording for allergy food or unwanted ingredients
#Setup for search
#Allergy:   input-free
#Unwanted:  -input
def checker(self, x):
    #splits the client inputs
    ch = x.split()
    #Allergies
    for i in len(ch):
        if ch == "gluten" | ch == "shellfish" | ch == "peanut" | ch == "dairy":
            self.Input.append(ch + "-free")
        #Uwanted Ingredients
        else:
            self.Input.append("-" + ch)



@app.route('/end', methods=['POST'])    
def end(self):
    #Convert list to String
    query = ' '.join(self.Input)
    #print out the google search result
    print(search(query, tld="co.in", num=1, stop=1))
    
    #Search for recipe 
    print("Have a good day")
    
if __name__ == '__main__':
    app.run(app, debug=True)
