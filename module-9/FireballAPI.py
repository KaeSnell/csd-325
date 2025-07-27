# Mikaela Snell
# July 27th, 2025
# Module 9.2 Assignmnet: APIs
# This program connects to the Fireball API and allows the user to lookup the number of fireballs in 2015 in a given month.

import requests
import json

url = "https://ssd-api.jpl.nasa.gov/fireball.api?date-min=2015-01-01&date-max=2015-12-31"

def connect_to_api(url):
  try:
    fireball = requests.get(url)
    if fireball.status_code == 200:
      print("Connection Status Code: ", fireball.status_code)
      return fireball.json()
    else:
      print("Error: Unable to connect to the API.")
      print("Status code: ", fireball.status_code)
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

# Creating a sample program that uses the API data
def search_month(data):
  month = input("Enter a number between 1 and 12 to lookup that month: ")
  
  months = {
      "01": "January",
      "02": "February",
      "03": "March",
      "04": "April",
      "05": "May",
      "06": "June",
      "07": "July",
      "08": "August",
      "09": "September",
      "10": "October",
      "11": "November",
      "12": "December"
  }
  
  while not month.isdigit() or not (1 <= int(month) <= 12):
    print("Invalid input. Please enter a digit between 1 and 12.")
    month = input()

  fields = data["fields"]
  date_index = fields.index("date")
  count = 0
  month = month.zfill(2)
  
  for entry in data["data"]:
      date_str = entry[date_index]
      month_str = date_str.split("-")[1]
      if month_str == month:
          count += 1

  print(f"\nNumber of fireballs in {months[month]}: {count}")


def main(data):
  
  print("Welcome to the Fireball API program!")
  print("This program will allow you to lookup the number of fireballs in 2015 in a given month.")
  search_month(data)
  print("\nDo you want to look up another month?\n")
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
  

