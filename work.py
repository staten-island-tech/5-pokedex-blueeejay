
    

    
# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
# def list():
#    for index, pokes in enumerate(data):
#         print(index, ":", data[index]["name"]) 
    

# Add a language choice feature and print the pokemons name based on the user input
""" import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
def lala():
 lang = input("What language would you like to view the pokemon names in? Choose from English, Japanese, Chinese, or French?:")

 if lang.lower() == "french": 
     for index, pokes in enumerate(data): 
         print(index, ":", data[index]["name"]['french'])
 if lang.lower() == "chinese": 
     for index, pokes in enumerate(data): 
         print(index, ":", data[index]["name"]['chinese'])
 if lang.lower() == "english": 
     for index, pokes in enumerate(data): 
         print(index, ":", data[index]["name"]['english'])
 if lang.lower() == "japanese": 
     for index, pokes in enumerate(data): 
         print(index, ":", data[index]["name"]['japanese'])
lala()
 """
 
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

# import json
# pokedex = open("./pokedex.json", encoding="utf8")
# data = json.load(pokedex)
# def typegetter():
#    typewant = [] 
#    x = 0
#    y = 0
#    type = input("What type of pokemon are you looking for? Capitalize the first letter:")
#    for  mon in (data):
#         if type in data[x]["type"]:
#             typewant.append(data[x]["name"]['english']) 
#         x = x =+ 1 
#    for i in (typewant):
#         print(y, ":", typewant[y]) 
# #         y += 1

import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
typeslist = open("./types.json", encoding="utf8")
typed = json.load(typeslist)


def typegetter():
    typewant = []
    mon = 0 # (current mons)
    for index, x in enumerate(typed):
            print(index, ":", typed[x]["type"]['english'])
            x = x + 1 
    chosen = int(input("Input the number corresponding to the type you are searching for:"))
    for mon in data:
            if chosen in data[mon]["type"]:
                typewant.append(data[mon]["name"]['english'])
            mon += 1 
    print(typewant)
typegetter() 
# #Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 
# def search():
#     charc = 0
#     x = 0 
#     ussearch = (input("Enter your search here: "))
#     totchar = len(ussearch)
#     for lettah in list(ussearch):
#         if lettah == list(ussearch[x]):
#             x += 1 
#             charc +=1 
#     if charc 
        
#For Leo/, help me come up with a clever final question, considering maybe showing all moves a pokemon has avaiable based on type
