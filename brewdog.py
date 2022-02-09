from numpy import append
import requests
import json
import ast

response = requests.get("https://api.punkapi.com/v2/beers")
beersdata = response.json()
abvpercentage = input("What beer ABV percentage or greater are you look for (e.g 6)? ")
TotalBeers = 0
beerList =[]
def myFunc(e):
  return e['ABV']

for beer in beersdata :
    if beer.get('abv') >= float(abvpercentage) :
        TotalBeers = TotalBeers + 1
        beerName = beer.get('name')
        abvVolume = beer.get('abv')
        beerdictionary = ast.literal_eval("{'Beer' : '" + beerName + "','ABV' : " f"{abvVolume}""}")
        beerList.append(beerdictionary)
beerList.sort(key=myFunc)
for sortedbeer in beerList:
    print(f" {sortedbeer['Beer']},{sortedbeer['ABV']}")
print(f"We have a total of {TotalBeers} beers that are a equal to or above {abvpercentage} % ABV")