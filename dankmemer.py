import random


pycoin = 0
fishingRod = False
rifle = False
dog = False
cat = False
dragon = False
pc = False
memeCoin = 0
petcoin = 0


class something():
    def multiply(self, yourcoin):
        if dog == True:
            return yourcoin * 1.25
        elif cat == True:
            return yourcoin * 1.5
        elif dragon == True:
            return yourcoin * 1.75
        else:
            return yourcoin 

Multiplier = something()

#this code is owned by shinchan.py#1455 and ImQWERTY#2374

#all code in here
while True:
    command = input().lower()

    # shows balance
    if command == "pls bal" or command == "pls balance":
        print(f"You have {pycoin} pycoin")

    # start begging
    if command == "pls beg":
        yourcoin = random.randint(1, 220)
        if yourcoin < 30:
            print("You got 0 pycoins")
        else:
            print(yourcoin)
            print(f"You got {Multiplier.multiply(yourcoin)}")

            

    # turn american.. i mean hunt animals
    if command == "pls hunt":
      if rifle == True:
        animals = random.randint(1, 100)
        if animals <= 5:
            print(f"You got a dragon!, you get 5000 pycoins from selling it")
            pycoin += Multiplier.multiply(5000)
        elif animals > 5 and animals < 10:
            print("You caught a random animal, take 2000 cause idk what it is :/")
            pycoin += Multiplier.multiply(2000)
        elif animals > 10 and animals < 50:
            print("You caught a dumb, you got 500 pycoins from selling it")
            pycoin += Multiplier.multiply(500)
        elif animals > 50: 
            print("You got a rabbit, you get 100 pycoins from selling it")
            pycoin += Multiplier.multiply(100)
      else:
        print("Buy a Hunting rifle!")


    #fishing 
    if command == "pls fish":
      if fishingRod == True:
        fish = random.randint(1, 100)
        rodBreak = random.randint(1, 10)
        if fish <= 5:
            print(f"You got a exotic fish!, you get 5000 pycoins from selling it")
            pycoin += Multiplier.multiply(5000)
        elif fish > 5 and fish < 10:
            print("You caught a legendary fish, take 2000 cause idk what it is :/")
            pycoin += Multiplier.multiply(2000)
        elif fish > 10 and fish < 50:
            print("You caught a rare fish, you got 500 pycoins from selling it")
            pycoin += Multiplier.multiply(500)
        elif fish > 50: 
            print("You got a fish, you get 100 pycoins from selling it")
            pycoin += Multiplier.multiply(100)
        elif rodBreak == 10:
          print("You broke your rod buy another one [has a 10% chance]")
          fishingRod = False 
      else:
        print("Buy a Fishing Rod!")

    #all commands
    if command == "pls help":
         print("""pls beg - beg money 
pls bal - shows bank balance
pls fish - does fishing and sells the fish 
pls hunt - hunts animals and sells it
pls postmeme - post a meme
pls highlow - guess number, nothing else :/
pls meme - tells you a joke
pls pet - can buy a pet
pls shop - buy the shop (jk) you can buy stuffs""") 

    #beting
    if command == "pls bet":
        bet = random.randint(1,2)
        if bet == 1:
            bet2 = random.randint(60, 300)
            print(f"You won {Multiplier.multiply(bet2)} pycoins")
            pycoin += bet2
        else:
            bet3 = random.randint(60, 300)
            print(f"You lost {bet3} pycoins , betting aint good kid")
            pycoin -= bet3

    #meme_OG
    if command == "pls meme":
        meme = random.randint(1, 10)
        if meme == 1:
            print("What do you call a fish with no eyes,         a fsh")
        elif meme == 2:
            print("What is the difference between you and a monkey, the letter u")
        elif meme == 3:
            print("School (thats the joke), jk you get 5 pycoins for hearing this pj")
            pycoin += 5
        elif meme == 4:
            print("")
        elif meme == 5:
            print("")
        elif meme == 6:
            print("")
        elif meme == 7:
            print("")
        elif meme == 8:
            print("")   
        elif meme == 9:
            print("")    
        elif meme == 10:
            print("")

      #posting meme 
    if command == "pls pm" or command == "pls postmeme":
      if pc == True:
        memeCoin = random.randint(100, 2000)
        breakChance = random.randint(1, 10)
        if breakChance == 10:
          print("You broke your PC for that dumb meme and got 0 pycoins , go buy a new one 'pls shop' ")
          pc = False
        else:
          print(f"You got {Multiplier.multiply(memeCoin)} from that meme's ads")
      else:
        print("Go buy a PC to post memes")    

    # high low, gonna be hard :c
    if command == "pls hl" or command == "pls highlow":
      guessNumber = random.randint(1, 100)
      hintNumber = random.randint(1, 100)
      userGuess = input(f"Guess if the number is lower, higher or equal to {hintNumber}: ").lower()
      if guessNumber < hintNumber:
        if userGuess == "lower" or userGuess == "l":
          yourcoin = random.randint(100, 500)
          print(f"You guess it correct, you earned {Multiplier.multiply(yourcoin)} pycoins")
          pycoin += Multiplier.multiply(yourcoin)
        else:
          print("Haha loser")
      if guessNumber > hintNumber:
        if userGuess == "higher" or userGuess == "h":
          yourcoin = random.randint(100, 500)
          print(f"You guess it correct, you earned {Multiplier.multiply(yourcoin)} pycoins")
          pycoin += Multiplier.multiply(yourcoin)
        else:
          print("Haha loser.")

      if guessNumber == hintNumber:
        if userGuess == "jackpot" or userGuess == "j":
          yourcoin = random.randint(500, 4000)
          print(f"You guess it correct, you earned {Multiplier.multiply(yourcoin)} pycoins")
          pycoin += Multiplier.multiply(yourcoin)
        else:
          print("Haha loser.")

      #shop
    if command == "pls shop":
       print("""We have 3 things in shop,
Hunting rifle (2000) 
Fishing Rod (2000)
PC (2000)
Type pls buy [item name] """)
    if command == "pls buy hunting rifle":
       if pycoin > 2000:
          print("You now have a hunting rifle")
          rifle = True
          pycoin =- 2000
       else:
          print("Get money poor guy")

    if command == "pls buy fishing rod":
       if pycoin > 2000:
         print("You now have a fishing rod")
         fishingRod = True
         pycoin -= 2000
       else:
         print("Get money poor guy")

    if command == "pls buy pc":
      if pycoin > 2000:
         print("You now have a PC")
         pc == True 
         pycoin -= 2000
      else:
         print("Get money poor guy")

     #cheat (for devs only)
    if command == "pls cheat":
       pycoin += 10000

     #pet
    if command == "pls pet":
         print("""Available pets are
Dog - 3000 , gives a 1.25x multiplier on any earnings      
Cat - 4000 , gives a solid 1.5x multiplier on any earnings
Dragon - 5000 , gives a extra solid 1.75x multiplier on any earnings
type pls pet [name of pet to buy]
         """) 
    if command == "pls pet dog":
       if pycoin > 3000:
         print("You now have a pet dog !")
         dog = True
         pycoin -= 3000
       else:
         print("Get money poor guy")
    if command == "pls pet cat":
       if pycoin > 4000:
         print("You now have a pet cat")
         cat = True
         pycoin -= 4000
    if command == "pls pet dragon":
       if pycoin > 5000:
        print("You now have a pet dragon")
        dragon = True
        pycoin -= 500

    #test (devs only) remember to remove it ok ._.
    if command == "pls test":
      pycoin += 1000000000
    if command == "pls clear" :
      pycoin = 0