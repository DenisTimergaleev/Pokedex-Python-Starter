import json
pokedex = open("./pokedex.json", encoding="utf8")
data = json.load(pokedex)
print(data[0])
language = input("What language would like to choose")
for pokemon in range (len(data)):
    if language == ("English"):
        print(data[pokemon]["Name"]["English"])
if language == ("Japanese"):
    print(data[pokemon]["Name"]["Japanese"])
if language == ("Chinese"):
    print(data[pokemon]["Name"]["Chinese"])
if language == ("French"):
    print(data[pokemon]["Name"]["French"])