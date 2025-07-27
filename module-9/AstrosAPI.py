# Mikaela Snell
# July 27th, 2025
# Module 9.2 Assignmnet: APIs
# This program connects to the Open Notify API and retrieves data about the astronauts currently in space.

import requests
import json

url = "http://api.open-notify.org/astros.json"

# Try connecting to the API
def connect_to_api(url):
  try:
    astronauts = requests.get(url)
    if astronauts.status_code == 200:
      print("Connection Status Code: ", astronauts.status_code)
      return astronauts.json()
    else:
      print("Error: Unable to connect to the API.")
      exit()
  except requests.exceptions.RequestException as e:
    print("Error: ", e)

# Following along https://www.dataquest.io/blog/api-in-python/ 
def json_print(obj):  
  text = json.dumps(obj, sort_keys=True, indent=4) 
  print(text)

def tutorial(data):
  print("\nAPI Info:\n", data)
  print("\nFormatted Info:")
  json_print(data)

# Creating a sample program to use the API data.

def unique_crafts(people):
  crafts = sorted(set(person["craft"] for person in people))
  return crafts

def craft_validate(crafts):
  """Validates the craft name entered by the user."""
  craft = input("> ")
  while craft not in crafts:
      print("Invalid craft.")
      print("Please enter a valid craft.")
      craft = input("> ")
  return craft

def people_on_craft(astronauts, craft):
  """Returns a list of people on the specified craft."""
  people = [person["name"] for person in astronauts["people"] if person["craft"] == craft]
  print("The", craft, "has the following people aboard it:\n")
  for person in people:
    print(person)
    
  print("\nThere are", len(people), "total people aboard the", craft,)

def main(data): 
  """Main function for the program."""
  crafts = unique_crafts(data["people"])
  
  print("There are currently " + str(len(crafts)) + " inhabited crafts in space.\n")
  print("Which craft do you want info for?\n")
  print("The inhabited crafts currently in space are:\n")
  for craft in crafts:
    print(craft)
  print()

  while True:
    print("Type the name of the craft you want to know more about.")
    selected_craft = craft_validate(crafts)
    people_on_craft(data, selected_craft)

    print()
  
    print("Do you want to know more about another craft?\n")
    print("Type no to exit or yes to continue.")
    answer = input("> ").lower()

    while answer not in ["yes", "no"]:
      print("Invalid input. Please enter yes or no.")
      answer = input("> ").lower()
      
    if answer == "no":
      print("Now exiting the program.")
      print("Goodbye!")
      exit()
    else:
      main(data)

     


if __name__ == "__main__":
  data = connect_to_api(url)
  main(data)
  # tutorial(data)
