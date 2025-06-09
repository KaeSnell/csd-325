# Mikaela Snell
# June 8th, 2025
# Module 1.3 Assingment: On the Wall
# This program demonstrates a recursive function that takes the 
# user through the song "99 Bottles of Beer on the Wall"

print("Welcome to the 99 Bottles of Beer on the Wall song!\n")

# Get the quantity of beers and validate the input
while True:
    try:
        quantity_of_beers = int(input("Enter the number of beers on the wall: "))
        if quantity_of_beers < 1:
            print("Please enter a number greater than 0.")
        else:
            break
    except ValueError:
        print("Please enter a valid integer.")

# Function that takes the user through the song.
def beers_on_wall(quantity_of_beers):
  if quantity_of_beers > 1:
    print(f"{quantity_of_beers} bottles of beer on the wall, {quantity_of_beers} bottles of beer.")
    print("Take one down, pass it around,")
    quantity_of_beers -= 1
    print(f"{quantity_of_beers} bottles of beer on the wall.\n")
    beers_on_wall(quantity_of_beers)
  else:
    print(f"{quantity_of_beers} bottle of beer on the wall, {quantity_of_beers} bottle of beer.")
    print("Take one down, pass it around,")
    quantity_of_beers -= 1
    print("No more bottles of beer on the wall.")

# Call the function
beers_on_wall(quantity_of_beers)

# End of program
print("\nTime to buy more beer!")