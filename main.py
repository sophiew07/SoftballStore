#-----------------------------------------------------------------------------
# Name:        Sophie's Softball Store (main.py)
# Purpose:     Learn about the user and try to sell softball products to the user
#
# Author:      Sophie Wong
# Created:     15-Feb-2023
# Updated:     24-Feb-2023
#-----------------------------------------------------------------------------
  
# batter function - learn information about user relating to batting and suggest bats
def batter():
  # determining if the user plays fast pitch or slow pitch, then recommending a bat
  fastOrSlow = str(input("Do you play fastpitch or slowpitch? "))
  fastOrSlowLower = fastOrSlow.lower()
  while fastOrSlowLower not in ["fastpitch","slowpitch"]:
      fastOrSlowLower = str(input("Input 'fastpitch' or 'slowpitch' "))
  if fastOrSlowLower in ["fastpitch"]:
    print("If you need a new bat, I would recommend the Easton Sapphire Fastpitch Bat for $109.99. Open the following link to view the product: https://www.sportchek.ca/categories/shop-by-sport/baseball-softball/baseball-softball-bats/softball-bats/product/easton-sapphire-12-fastpitch-bat-color-333755186_10-333755186.html#333755186%5Bcolor%5D=333755186_10")
  elif fastOrSlowLower in "slowpitch":
    print("If you need a new bat, I would recommend the Miken Psycho Maxload Slowpitch Bat for $224.97 (it's on sale!). Open the following link to view the product: https://www.sportchek.ca/categories/shop-by-sport/baseball-softball/baseball-softball-bats/softball-bats/product/miken-psycho-maxload-19-1-piece-slowpitch-bat-333071322.html#")
  print()
  # number of homeruns
  numberOfHomeRuns = int(input("How many home runs have you hit in total? "))
  while numberOfHomeRuns < 0:
    numberOfHomeRuns = int(input("That makes no sense... Try again. "))
  if numberOfHomeRuns >= 1:
    print("That's impressive! You must swing pretty hard, so maybe getting a new bat wouldn't be a bad idea.")
  elif numberOfHomeRuns == 0:
    print("That's alright, you'll get one soon!")
  print()
  print("I'm curious about your most recent game. Tell me how many runs your team scored in each inning. ")

# determining how many runs were scored in the user's previous game
  runsInTheInningTotal = 0
  for inning in range(1,8):
    runsInTheInning = int(input("Inning " + str(inning) + ": "))
    while runsInTheInning < 0:
      runsInTheInning = int(input("Input a positive number."))
    runsInTheInningTotal = runsInTheInningTotal + runsInTheInning
  print("Wow! Your team scored " + str(runsInTheInningTotal) + " runs!")
  print()
  
# pitcher function - learn information about user and suggest gloves
def pitcher():
  # leftie or rightie
  dominantHand = str(input("Are you left handed or right handed? "))
  dominantHandLower = dominantHand.lower()
  while (dominantHandLower not in ["left handed"]) and (dominantHandLower not in ["right handed"]):
    dominantHandLower = str(input("Your answer couldn't be processed. Type 'left handed' or 'right handed' ")) 
  # if left hand, recommend a left handed glove
  if dominantHandLower in ["left handed"]:
    print("That's cool! You're a part of the 12% of softball players who play left handed. If you need a glove, I would suggest buying the Wilson 12.5'' A950 Series Fastpitch Glove for $99.99. Open the following link to view the product: https://www.dickssportinggoods.com/p/wilson-12-5-a950-series-fastpitch-glove-22wilw950125fpl22bas/22wilw950125fpl22bas")
    print()
    # ask user if they want another option for left handed gloves
    anotherLeftGloveOption = str(input("Would you like to see another option? "))
    anotherLeftGloveOption = anotherLeftGloveOption.lower()
    while anotherLeftGloveOption not in ["yes","no"]:
      anotherLeftGloveOption = str(input("Try putting 'yes' or 'no' "))
    if anotherLeftGloveOption in ["yes"]:
      print("No problem! Why don't you try the Mizuno Premier 14'' Softball Glove for $109.99. Click this link to view the product: https://www.baseballtown.ca/us/gpm1405-premier-14-softball-glove.html")
    elif anotherLeftGloveOption in ["no"]:
      print("Alright, let's move on.")
      print()
  # if right hand, recommend right handed gloves
  elif dominantHandLower in ["right handed"]:
    print("Nice! Most softball players are right handed as well. If you need a glove, I would suggest buying the Wilson 12.5'' A950 Series Fastpitch Glove for $99.99. Open the following link to view the product: https://www.dickssportinggoods.com/p/wilson-12-5-a950-series-fastpitch-glove-22wilw950125fpl22bas/22wilw950125fpl22bas")
    print()
  # ask user if they want another option for right handed gloves
    anotherRightGloveOption = str(input("Would you like to see another option? "))
    anotherRightGloveOption =  anotherRightGloveOption.lower()
    while anotherRightGloveOption not in ["yes","no"]:
        anotherRightGloveOption = str(input("Try putting 'yes' or 'no' "))
    if anotherRightGloveOption in ["yes"]:
      print("No problem! Maybe try the Easton Prime I-Web 11.5'' Softball Glove that's on sale right now for $59.97. Click this link to view the product: https://www.sportchek.ca/categories/shop-by-sport/baseball-softball/baseball-bats-gloves/product/easton-prime-i-web-115-softball-glove-right-hand-catch-slowpitch-333563228.html#")
    elif anotherRightGloveOption in ["no"]:
      print("Alright, let's move on.")  
      print()
    
# listing products for user to select and purchase
def userSelect():
  print("CHECKOUT")
  print("1. Easton Sapphire Fastpitch Bat")
  print("2. Miken Psycho Maxload Slowpitch Bat")
  print("3. Wilson 12.5'' A950 Series Fastpitch Glove")
  print("4. Mizuno Premier 14'' Softball Glove")
  print("5. Easton Prime I-Web 11.5'' Softball Glove")
  print()
  userPurchase = str(input("Do you want to purchase a product? "))
  userPurchase = userPurchase.lower()
  print()
  while userPurchase not in ["sure","no thanks"]:
    userPurchase = str(input("Try putting 'sure' or 'no thanks' "))
  if userPurchase in ["sure"]:
    userPurchase = int(input("Great! You can tell me which product you want by telling me the corresponding number. "))
    while userPurchase != 1 and userPurchase != 2 and userPurchase != 3 and userPurchase != 4 and userPurchase != 5:
      userPurchase = int(input("Try putting '1' '2' '3' '4' or '5' "))
    userShoppingCart = 0
# adding user selection to shopping cart, then telling user what their total is and how much money they have left
    if userPurchase == 1 or userPurchase == 4:
      userShoppingCart = userShoppingCart + (109.99*1.13)
    elif userPurchase == 2:
      userShoppingCart = userShoppingCart + (224.97*1.13)
    elif userPurchase == 3:
      userShoppingCart = userShoppingCart + (99.99*1.13)
    elif userPurchase == 5:
      userShoppingCart = userShoppingCart + (59.97*1.13)  
    userShoppingCart = round(userShoppingCart,2)
    userShoppingCart = userShoppingCart - 20
    userMoney = userBudget - userShoppingCart
    userMoney = round(userMoney,2)
    if userMoney < 0:
      print("Sorry, you can't purchase this product. ")
    else:
      print("After giving you a first time discount of $20, your total is $" + str(userShoppingCart) + ". Now you have $" + str(userMoney) + " remaining.")
    print("Thanks for coming! I hope to see you again :) ")
  if userPurchase in ["no thanks"]:
    print("Thanks for coming! I hope to see you again :) ")
    
# determining the user's familiarity with softball 
numberOfSeasons = int(input("Welcome to Sophie's Softball Store! Just so I can get to know you, how many seasons have you played? "))
while numberOfSeasons < 0:
  numberOfSeasons = int(input("That's impossible, try again. "))
if numberOfSeasons == 0:
  print("Cool! I'm guessing you just started.")
elif numberOfSeasons >= 1 and numberOfSeasons <= 3:
  print("Nice! I assume you're a rookie.")
elif numberOfSeasons >= 4 and numberOfSeasons <= 20:
  print("Wow! You're basically a professional softball player.")
else:
  print("I've never seen someone play so many seasons!")

# determining user's budget for softball equipment
userBudget = float(input("So, what's your budget today? "))
userBudget = round(userBudget,2)
while userBudget < 0:
  userBudget = float(input("That can't be your budget... Go again. "))
while userBudget >= 0.01 and userBudget <= 254.22:
  userBudget = float(input("Not sure if you have enough to purchase some things, come back when you have more money... So how much do you have now? "))
  while userBudget < 0:
    userBudget = float(input("That can't be your budget... Go again. "))
if userBudget == 112.99 or userBudget == 254.22 or userBudget == 124.29:
  print("Well, I've got the perfect products within your budget!")
elif userBudget >= 254.23 and userBudget <= 500 and userBudget not in (112.99,254.22,124.29):
  print("You came well prepared to buy softball products! Let me help you find the right equipment :) ")
else:
  print("Where'd you get all that money from... You didn't rob a bank, did you? Anyways, I'll try and help you find the right product. ")

# determine user's position
position = str(input("Are you a batter or pitcher? "))
positionLower = position.lower()
while positionLower not in ["batter","pitcher"]:
  positionLower = str(input("Your answer couldn't be processed, put 'batter' or 'pitcher' "))

# if user is a batter
if positionLower in ["batter"]:
  batter()
  anotherPosition = str(input("Do you pitch as well? "))
  anotherPosition = anotherPosition.lower()
  while anotherPosition not in ["yes","no"]:
    anotherPosition = str(input("Try putting 'yes' or 'no' "))
  if anotherPosition in ["yes"]:
    pitcher()
  elif anotherPosition in ["no"]:
    print("Let's go to the checkout.")
  print()
  userSelect()
# if user is a pitcher
elif positionLower in ["pitcher"]:
  pitcher()
  anotherPosition = str(input("Do you bat as well? "))
  anotherPosition = anotherPosition.lower()
  while anotherPosition not in ["yes","no"]:
    anotherPosition = str(input("Try putting 'yes' or 'no' "))
  if anotherPosition in ["yes"]:
    batter()
  elif anotherPosition in ["no"]:
    print("Let's go to the checkout.")
  print()
  userSelect()
