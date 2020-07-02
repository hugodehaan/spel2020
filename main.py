import random
def spel() :

  # de woorden die gebruikt gaan worden
  woordenlijst = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier",
  "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", "heesterperk"]
  # random woord word gekozen en door puntjes vervangen 

  hetwoord= random.choice(woordenlijst)
  lengtewoord = len(hetwoord)
  puntjes = [" ~ "] *lengtewoord
  ja = "ja"
  nee = "nee"

  # introductie
  naam = input("Vul hier je naam in: ")
  print()
  print("Welkom", naam,"bij ons galgje spel")
  game = True

  print("Raad de letters en als je het woord weet typ het dan in.")
  print()
  print("het woord heeft " + str(lengtewoord) + " letters")

  while game == True:
    userGuess = input("geef letter/woord> ")
    # zit letter in woord? Zo ja, waar dan?

spel()
