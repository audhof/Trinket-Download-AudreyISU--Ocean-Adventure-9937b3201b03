'''
Name: Audrey
Date: Monday, May 12, 2025
Title: ISU- Ocean Adventure
'''

#Introduction to the Game
print ("Ahoy Captain Blackbeard and welcome to Ocean Adventure! Your arch-nemesis Scarface who was responsible for giving you a peg leg has come back for revenge and convinced your crew to betray you. Your ship is stolen and you have nothing. Now you must enact revenge and take back what is rightfully yours. If you wish to take back your ship you must find the ancient shipwreck 'The Lost Alondra' containing a magical artifact giving the user supernatural abilities and endless treasure. This journey will be filled with challenges, but you can do it!")

#Create a 2D list with all your rooms
roomlist= []

#room=["Room 0- Description(add your own)", North, East, South, West]
room = ["\nRoom 0- Beach: Sandy beach with rocky terrain to your right and a sand castle and beach umbrella. The water is cold and murkey", None,1,None, None]
roomlist.append(room)

#repeat this for all the rooms
room = ["\nRoom 1- Ocean Cave: A dark cave containing bones and a skeleton, a warning sign and a large, glowing octopus", 2, 4, None, 0]
roomlist.append(room)

room = ["\nRoom 2 - Glowing Lagoon: A glowing large body of water with a terrifying sea monster, sharp rocks and a hidden sword", None, 3,1, None]
roomlist.append(room)

room = ["\nRoom 3- Coral Reef: Surrounded by colourful, bright coral, a school of tropical fish and a large clam", None, None, 4,2]
roomlist.append(room)

room= ["\nRoom 4- Underwater Palace : A beautiful throne room with the intimidating King Neptune holding a trident sitting on a regal throne", 3, None, 5, 1]
roomlist.append(room)

room = ["\nRoom 5- Shipwreck : A broken down shipwreck containing a large treasure chest and glowing purple gemstone",4 , None, None, None]
roomlist.append(room)

#Initialize variables
current_room = 0
done = False

#function for direction
def move(current_room, direction):
  directions = {"n": 1, "e": 2, "s": 3, "w": 4} 
  next_room = roomlist[current_room][directions.get(direction, -1)]

  if next_room is None:
    print("There is no pathway.")
    return current_room  # Stay in the same room
  else:
    print(roomlist[next_room][0])
    return next_room  # Move to the new room
        
#Set up a while loop for your game navigation
while done==False:
  
  #Challenge in room #0 is to find the treasure map
  #empty 2D list
  beach = []
  beach.append(["Rocks", "Sand", "Ocean"])
  beach.append(["crab", "shells", "fish"])
  beach.append(["geode", "umbrella", "pelican"])
  beach.append(["seagull", "burried item", "blurry thing"])
  beach.append(["box", "sand castle", "rocks"])
  
  if current_room == 0:
    print("\n\nYou must first find the hidden treasure map on the beach in order to move on with your journey.")
    for row in beach: 
      print('| {:^15} | {:^15} | {:^15}'.format(*row))
    
    search = str(input("Pick a place to search first: "))
    while search!= "blurry thing":  #loop to repeat search
      if search == "box":
        print("Good guess but the box was empty")
        search = input("Pick a new place to search: ")
      elif search == "burried item":
        print("Oooooh a message in a bottle. Could this be the map? Unfortunately it looks like a love note.")
        search = input("Pick a new place to search: ")
      else:
        print("Hmmm... Looks like theres nothing there, keep looking!")
        search = input("Pick a new place to search: ")
    
    print("Nice! It looks like the blurry thing in the ocean was the treasure map and it says you have to go East to the ocean cave next.")
    hasmap = True
  
  direction = input("\nWhich direction would you like to go? (n,e,s,w): ")
  current_room = move(current_room, direction)  # Call the function
  
  #Room 1- find clues
  if current_room == 1:
    print("\nWelcome to the Ocean Cave. There's no challenge to be completed but there are clues to be found before moving on...")
    
    #Dictionary
    cave = {"octopus": "\nOctopus: 'It has been many years since I have seen another attempt this journey, the last one  did not survive. But if you wish to continue on this journey, you should go North to the glowing lagoon.'" , "bones" : "\nLooks like these are the remains of the last person who attempted this journey... spooky.", "sign": "\nWarning! Turn Back Now, Before It's Too Late!"}
    
    #Clues
    caveclue = str(input("What do you want to look at? The octopus, sign or the bones: "))
    while caveclue != "octopus":  #loop for search
      if caveclue == "sign":
        print(cave["sign"])
        caveclue = str(input("What do you want to look at next? The octopus or the bones: "))
      elif caveclue == "bones":
          print(cave["bones"])
          caveclue = str(input("What do you want to look at next? The sign or the octopus: "))
      else: 
          print("invalid input...")
          caveclue = str(input("What do you want to look at? The octopus, sign or the bones: "))
      
    print(cave["octopus"])
 
 #Room 2-Defeat sea monster
  if current_room ==2:
    print("\nIn order to move on to the next place in your journey, you must defeat the enormous sea monster. You have three choices, \n1. attack using tools you have \n2. defend \n3. find the hidden weapon and attack")
    
    #Variables
    monsterhealth = 10
    playerhealth = 10
    
    while monsterhealth > 0 and playerhealth > 0: 
      choice = input("Choose an action (1,2, or 3): ")
      import random
      
      if choice == "1":
        damage = random.randint (1,3)
        monsterhealth -= damage
        print('You attack with your metal hook and deal' , (damage), 'damage! The monster has' , (monsterhealth), 'health left.')
      elif choice == "2":
        block = random.randint(1,2)
        playerhealth+= block
        print('You defend and regain', (block), 'health! You now have ', (playerhealth), 'health.')
      elif choice == "3":
        damage = random.randint(3,6)
        monsterhealth -= damage
        print('You get the sword and deal', (damage), 'damage! The monster has', (monsterhealth), 'health left.')
      else:
        print("invalid choice, try again!")
      
      if monsterhealth >0:
        hit = random.randint(1,4)
        playerhealth -= hit
        print('The sea monster attacks and deals ', (hit), 'damage! You have ', (playerhealth), 'health left')
  
    if monsterhealth <= 0:
      print("You have defeated the sea monster! Congratulations, you may now continue on your journey! Move east to the coral reef.")
    elif playerhealth <= 0:
      print("The sea monster defeated you... You must respawn and try again. Enter n")
      current_room -=1
  
  # Room 3-Find clues
  if current_room == 3:
    print("\nWelcome to the coral reef, there are no challenges to complete here but you must find a clue in order to find out where to go next.")
    #Dictionary
    coral = {"coral" : "\nLooks like theres nothing here, but it sure is pretty!" , "fish" : "\nFish: Hey good job defeating that sea monster we heard all about it from a dolphin, we don't have any clues for you though. Maybe ask the clam?" , "clam" : "\nClam: In order to find what you seek you must go South and meet with King Neptune. Be careful though, I hear he's feeling a bit blue. "}
    
    coralclue = str(input("What do you want to investigate? coral/clam/fish: "))
    while coralclue != "clam":
      if coralclue == "coral":
        print (coral["coral"])
        coralclue = str(input("What do you want to investigate next? clam/fish: "))
      elif coralclue == "fish":
        print(coral["fish"])
        coralclue = str(input("What do you want to investigate next? coral/clam: "))
      else:
        print("invalid input")
        coralclue = str(input("What do you want to investigate? coral/clam/fish: "))
    
    print(coral["clam"])
  
  #Room 4- Riddle
  if current_room == 4:
    print("\nKing Neptune: Greetings! You have come quite far on your journey to find the ancient shipwreck. But this will be the last and true test of your dedication and worthiness. You must answer an impossible riddle. If you are right I will grant you access to the treasure you seek, if you're wrong you will live out the rest of your days serving my kingdom!\n")
    
    #Input and Output files
    #read input file
    with open("input.txt","r") as file:
      riddle = file.read().strip()
    
    print(riddle)
    useranswer = input("Your answer: ").lower()
    
    correctanswer = "blue"
    #Check the answer and write result in output.txt
    result = "King Neptune: Wow consider me suprised, no human has ever passed my riddle. Congratulations. Your prize is located to the south." if useranswer == correctanswer else "King Neptune: Unfortunately that answer is wrong.You should pay closer attention when you are given clues, I am disapointed in you. My 12th daughter's name is " + correctanswer
    
    if useranswer!= correctanswer:
      done = True
    with open("output.txt", "w") as output: 
      output.write (result)
    
    print (result)
    
    #Close input and output files
    output.close()
    file.close()
  #Final room- get treasure
  if current_room == 5:
    print ("\nCongratulations Captain, you've done it, all your hard work has paid off! This place is amazing, and it has everything you could have ever wanted! The treasure chest is filled to the brim with gold. It has more than you will ever need. And the magical artifact is glowing so bright, you can feel the power coming off of it. You grab the artifact and immediately feel the supernatural strength enter your body, next you go to fill your pockets with gold. Now all thats left is to decide what to do with this newfound power...")
    end = str(input("\nWhat will you do now? 1) buy a new ship and explore the sea 2) live the rest of your life in relaxation on a beautiful beach cabin 3) seek revenge on scarface and your cowardly crew: "))
    if end == "1": 
      print (" Ten years later... \n You decided to buy a new ship and explore the sea, you discovered new land and your name went down in history as a monumental explorer. You maintained great relationships with the people you met along the way including King Neptune who invites you over for a great feast a couple times a year.")
      done = True
    elif end == "2":
      print("Ten years later... \n You decided to relax on the beach for the rest of your life. You never made any great achievements and your name didn't go down in history, but you always feel at peace and you made new friends with your neighbours. You later found out that Scarface died in a sea raid. ")
      done = True
    elif end == "3":
      print("5 years later... \n You decided to seek revenge against scarface, and you got it but at what cost? You fought scarface and your crew and they died in the battle but in the process your precious ship was destroyed. In the end you got revenge but no real satisfaction. At least you are now known as the infamous pirate who defeated scarface and an entire crew all on his own...")
      done = True

again = str(input("Game Over... Thank you for playing!"))


