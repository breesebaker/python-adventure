import os 
from time import sleep 
import logging 

logging.basicConfig(filename="adventureLog.log", level=logging.DEBUG)

def beggining():
  start_adventure = input("Hello Hungry Houstonian! Are you hungry? ")
  if start_adventure == "yes":
    very_hungry()
  elif start_adventure == "no":
    print("Come back when your hungry!!")

  very_hungry()

def very_hungry():
  hunger_one = input("where would you like to go? Choose from the following options: Mexican, Indian, American, Southeast Asian ") 
  if hunger_one == "mexican":
    mexican_food = input("You chose Mexican, Good choice! Here are some of my favorite spots. Which one sounds good? Picos, Hugos or Ninfas ")
    if mexican_food == input("Picos"):
      print("Picos is my favorite authentic Mexican in town!")
      print("They are located in the Upper Kirby area at 3601 Kirby Dr, Houston, Tx 77098")
    elif mexican_food == input("Hugos"):
      print("If your looking for authentic mexican food from an award winning chef, look no further!")
      print("Located in Houstons' historic Montrose area, thier address is 1600 Westheimer, Houston, Tx 77006")
    elif mexican_food == input("Ninfas"):
      print("Welcome to the birthplace of fajitas! Ninfas is Houstons most popular Mexican restuarant in the city!")
      print("Head on over to Houstons's East Downtown area to 2704 Navigation Blvd, Houston, Tx 77003")
      #possible return
  elif hunger_one == "indian":
    indian_food = input("You chose Indian food! Theres nothing like vindaloo and fresh garlic na'an! Which one sounds good? Shivas, Aga's or Khyber ")
    if indian_food == input("Shivas"):
      print("If your looking for some quick and easy, authentic southern indian stye food Shivas is the place for you!")
      print("Located in the West University area of Houston, Shiva offered home cooked, authentic delicious food. Thier address is 5220 Buffalo Speedway, Houston, Tx 77005")
    elif indian_food == input("Agas"):
      print("Aga's is by far my favorite place for anyhting Indo-Pak. They are a little ways away from where I live but oh so worht the drive!")
      print("If your looking for a more upscale authentic Indian food experience for special occasions. They are located at 11842 Wilcrest Dr, Houston, Tx, 77031")
    elif indian_food == input("Khyber"):
      print("Some of my favorite northen Indian food in town. Khyber offers some of the best butter chicken and vindaloos!")
      print("Head over to Houston's Upper Kirby neighboorhood to try them out! Their address is 2510 Richmond Ave, Houston, Tx, 77098")      
      #possible return
  elif hunger_one == "american":
    american_food == input("You chose American food! Out of my most frequently visited, which one sounds good? Graces, Empire Cafe or Truth BBQ ")
    if american_food == input("Graces"):
      print("When it comes to some american southern food, Grace's is by far one of the best in town. Try the Rosies fried chicken!")
      print("Another gem hidden in Houstons' Upper Kirby neighborhood, you can head on over to 3111 Kirby Dr, Houston, Tx 77098")
    elif american_food == input("Empire Cafe"):
      print("A Houston staple! Empire Cafe is a place everyone needs when in search of oversized breakfast plates and unlimited amount of fresh coffee!")
      print("Empire is located in Houstons historical Montrose district in what used to be a gas station. Thier address is 1732 Westheimer Rd, Houston, Tx 77098")
    elif american_food == input("Truth BBQ"):
      print("hailed as one of the best BBQ spots in the state, Truth's brisket alone is worth standing in line for.")
      print("Truth is located in the Heights neighboor hood just south of I-10 at 110 S Heights Blvd, Houston, Tx, 77007")
      #possible return

  elif hunger_one == "southeast asian":
    thai_food = input("You chose Southeast Asian Food! Which of these amazing places from thailand to vietnam would you like to try? (Rim Tanon, Kin Dee, Lua Viet ")
    if thai_food == input("Rim Tanon"):
      print("Want all the street food that Thailand has to offer without the jetlag? Look no further than Rim Tanon!")
      print("Rim Tanon bring Thai street food to your own backyard! Check them out at 2241 Richmond Ave, Houston, Tx, 77098")
    elif thai_food == input("Kin Dee"):
      print("Kin Dee offers some of the best homecooked thai food in Houston. Chef Miranda incorporates some of her favorite dishes from her home in Thailand")
      print("Head of to the Houston Height just south of the north loop to Kin Dee. Their address is 1533 N Shepherd Dr, Houston, Tx 77008")
    elif thai_food == input("Lua Viet"):
      print("My absolue favorite spot for Vietnamsese food! Lua Viet offers locally sourced ingredients and a welcome atmosphere for any occasion!")
      print("Lua Viet can be found in Houstons Montrose district at 1540 W Alabama St, Houston, Tx 77006 ")  
    
beggining()