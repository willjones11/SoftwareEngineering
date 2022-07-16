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
    self.QuesB = [["Do you want a certain cuisine?", "Do you want fruit in your dish?", "Pancakes?", "Waffles?", "Do you want chocolate in your dish?"], ["Do you want a certain cuisine?", "Do you want meat in your dish?", "Do you want a sandwich-like dish? (Sausage biscuit, bagel sandwich)", "Do you want eggs?",
     "Do you want vegetables?"]] #[0]= sweet [1]=savory #Breakfast
    self.QuesL = [["Do you want a certain cuisine?", "Would you like a salad?" "Would you like a sandwich?", "Do you want a rice dish?", "Do you want a soup dish?", "Do you want a noodle dish?", "Do you want vegetables?", "Do you want meat?"], ["Do you want a certain cuisine?", "Do you want a rice dish?", "Do you want a soup dish?", "Do you want a noodle dish?", "Do you want vegetables?", "Do you want meat?"]] #Lunch and Dinner
    self.QuesD = [] #Dessert
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
    ans = input("Are we looking for Breakfast, Lunch, Dinner, or Dessert?") #interaction to narrow down the list of questions to ask 
    self.Input.append(ans)
    if self.Input[0] == "Breakfast":
        breakfast()
    elif self.Input[0] == "Lunch" | self.Input == "Dinner":
        dunch()
    elif self.Input[0] == "Dessert":
        dessert()

@app.route('/breakfast', methods=['GET', 'POST'])
def breakfast(self):
    #checks for allergies 
    print("Any food allegries or food to avoid")
    x = input()
    checker(x)
    ans = input("Do you want sweet or savory meal?")
    self.Input.append(ans)
    if ans == "savory":
        for i in range(0, len(self.QuesB[1][1:])):
            print(self.QuesB[1][i])
            an = input()
            #if user wants to see their food answer from ric-bot
            if an == "result":
                break
            print(self.QuesB[1][i])
            ans = input().split()
            self.Input.extend(ans)

        
    if ans == "sweet":
        for i in range(0, len(self.QuesB[0][1:])):
            print(self.QuesB[0][i])
            an = input()
            #if user wants to see their food answer from ric-bot
            if an == "result":
                break
            print(self.QuesB[0][i])
            ans = input().split()
            self.Input.extend(ans)
    
    end()

@app.route('/dunch', methods=['GET', 'POST'])
def dunch(self):
     #checks for allergies 
    print("Any food allegries or food to avoid?")
    x = input()
    checker(x)
    ans = input("Do you want sweet or savory meal?")
    self.Input.append(ans)
    if ans == "savory":
        for i in range(0, len(self.QuesL[1][1:])):
            print(self.QuesL[1][i])
            an = input()
            #if user wants to see their food answer from ric-bot
            if an == "result":
                break
            print(self.QuesL[1][i])
            ans = input().split()
            self.Input.extend(ans)

        
    if ans == "sweet":
        for i in range(0, len(self.QuesL[0][1:])):
            print(self.QuesL[0][i])
            an = input()
            #if user wants to see their food answer from ric-bot
            if an == "result":
                break
            print(self.QuesL[0][i])
            ans = input().split()
            self.Input.extend(ans)
    end()

app.route('/dessert', methods=['GET', 'POST'])
def dessert(self):
     #checks for allergies 
    print("Any food allegries or food to avoid")
    x = input()
    checker(x)
    for i in range(0, len(self.QuesB[0][1:])):
        print(self.QuesB[0][i])
        an = input()
        #if user wants to see their food answer from ric-bot
        if an == "result":
            break
        print(self.QuesB[0][i])
        ans = input().split()
        self.Input.extend(ans)
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
