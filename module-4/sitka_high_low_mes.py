#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Mikaela Elizabeth Snell
# June 22nd, 2025
# Assignment 4.2: High/Low Temperatures
# This is a modified version of the sitka_weather.py file
# modified to be interactive, and allow the user to see the low temps as well.

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

# Added: Open the program with instructions for the user
print("Hello! Welcom to the high/low graphing program.")
print("This program allows you to graph the temperature for Sitka, Alaska.")
print("Enter 'high' or 'low' to choose which "
      "graph you would like to see, or 'exit' to quit.")

# Added: Function to get user choice
def get_choice():
    choice = input("> ")
    choice = choice.lower()
    return choice

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    # Changed: Added low temperatures
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)


# Added: process to ensure the graphs showed the same range, to further emphasize
# the difference between the highs and the lows
min_temp = min(min(highs), min(lows))
max_temp = max(max(highs), max(lows))

# Plot the high temperatures.
# plt.style.use('seaborn')
# Changed: turned the high temp graph into a function to be called
def high_graph():
  fig, ax = plt.subplots()
  ax.plot(dates, highs, c='red')

# Format plot.
  plt.title("Daily high temperatures - 2018", fontsize=24)
  plt.xlabel('', fontsize=16)
  fig.autofmt_xdate()
  plt.ylabel("Temperature (F)", fontsize=16)
  plt.tick_params(axis='both', which='major', labelsize=16)
  # Added: more formating
  plt.ylim(min_temp, max_temp)  

# Added: function for the low temp graph, modeled after the high temp code
def low_graph():
  fig, ax = plt.subplots()
  ax.plot(dates, lows, c='blue')

  plt.title("Daily low temperatures - 2018", fontsize=24)
  plt.xlabel('', fontsize=16)
  fig.autofmt_xdate()
  plt.ylabel("Temperature (F)", fontsize=16)
  plt.tick_params(axis='both', which='major', labelsize=16)
  plt.ylim(min_temp, max_temp) 

# Added: while loop to allow the user to select the graphs they want to see and exit when done
while True:
    print("\nPlease enter your choice")
    choice = get_choice()
    
    if choice == 'high':
        high_graph()
        plt.show()
    elif choice == 'low':
        low_graph()
        plt.show()
    elif choice == 'exit':
        print("Now exiting the program. Thank you and goodbye!")
        sys.exit()
    else:
        print("Sorry, we couldn't understand that. Please enter 'high', 'low', or 'exit'.")


# In[ ]:




