#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Mikaela Snell
# June 8th 2025
# Assignment 2.2: Documenting Debugging
# Originally an Intro to Python Assignment, modified for the purposes of debugging

# This program will take the full name of the user and return that persons initials.
def main():
  #Get the users full name.
  full_name = input("Enter your full name: ")
  # Split the input into separate strings.
  name_list = full_name.split()

  print("Your initials are: ", end='')
  # Get the initials of each name in the input.
  for name in name_list:
    # Check if the part being printed is the last name.
    if name is name_list[-1]:
      print(name[0].upper() + '.', end='')
    else:
      print(name[0].upper() + '.', end=' ')


# Call the main function.
if __name__ == '__main__':
  main()

