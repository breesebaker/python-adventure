


def introduction():
  print("|-----------------------------------------------------------------------------------------------------------|")  
  print("|                                      Welcome to the Houston Food Selector!                                |") 
  print("|-----------------------------------------------------------------------------------------------------------|") 
  print("") 
  print("") 
  print("") 
  print("") 
def beggining():
  start_adventure = input("Are you hungry?")
  if start_adventure == "yes":

#loop back
#not valid answer

    mid()  

def mid(): 
  first_choice = input("Your at the drivethrough of a McDonalds. You are very hungry and want to get your usual order, a 30 pack of chicken nuggets and get back home and enjoy them. But you see that the McRib is back. Which do you choose? (McRib/Nuggets)")   
  if first_choice == "mcrib":
    secound_choice = input("You order a McRib but are considering getting two because they are a limited time thing. Do you get one or two?")
    if secound_choice == "two":
      print("That second McRib was a bad choice and you get food poisoning")
    else:
      print("You are home enjoying your single McRib. But now your craving something sweet... TO BE CONTINUED")

  elif first_choice == "nuggets":
    print("You made the right choice and are happily on your way home to enjoy you snack")

  else:
    print("Come back when your ready!")

beggining() 

# story script:
# general idea - pull form a book(LOTR)/video game/random adventure based in houston/scary story?


Are you hungry? (Yes/No)

  Yes?
    Where would you like to go? (Mexican, Indian, American, Thai, Vietnamese)

    Mexican
      Where would you like to go? (Picos, Little Papasitos, Ninfas)
        Picos (Address, Phone Number)
        Little Papasitos (Address, Phone Number)
        Ninfas (Address, Phone Number)
      Return

    Idian
      Where would you like to go? (Shivas, Khyber, Kirans, Agas)
        Shivas (Address, Phone Number)
        Khyber Papasitos (Address, Phone Number)
        Kirans (Address, Phone Number)
        Agas (Address, Phone Number)
      Return

    American
      Where would you like to go? (Graces, Moxies, Mias Table, Roost)
        Graces (Address, Phone Number)
        Moxies (Address, Phone Number)
        Mias Table (Address, Phone Number)
        Roost (Address, Phone Number)
      Return

    Thai
      Where would you like to go? (Rim Tanon, Thai Bistro, Street Food Thai Market, Kin Dee)
        Rim Tanon (Address, Phone Number)
        Thai Bistro (Address, Phone Number)
        Street Food Thai Market (Address, Phone Number)
        Kin Dee (Address, Phone Number)
      Return

    Vietnamese
      Where would you like to go? (Lua Viet, Pho Siagon, Kua Ba, Fat Bao)
        Lua Viet (Address, Phone Number)
        Pho Siagon (Address, Phone Number)
        Kua Ba (Address, Phone Number)
        Fat Bao (Address, Phone Number)
      Return


No?
  Come back when you are hungry!