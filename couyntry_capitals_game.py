# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 11:41:36 2023

@author: Davronov Dilshod
"""

import random
import sys
from cou_cap_eng import countries_dict

# Function to run the game
def play_game():
    
    while True :
       # Convert the city-capital dictionary into a list of tuples
       city_capitals_list = list(countries_dict.items())

       # Shuffle the list of city-capital pairs
       random.shuffle(city_capitals_list)

       # Iterate through each city-capital pair
       for country  , capital in city_capitals_list:
           # Ask the user for the capital of the city
           guess = input(f"What is the capital of {country}? ")

           # Convert the user's guess to lowercase for case-insensitive comparison
           guess = guess.lower()

           # Compare the user's guess with the actual capital (case-insensitive)
           if guess == capital.lower():
               print("Correct!")
           else:
               print(f"Wrong! The capital of {country} is {capital}.")
               #asking user if wanna play again 
           answer = input('do you want to play again? (yes/no)')
           
           if answer != 'yes':
               #whenenver answer is not equal to yes that something
               #like nope, no it breakes the program
              print('have a good day or night')
              sys.exit()
              
      
# Run the game
play_game()

