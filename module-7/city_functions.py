# Mikaela Snell
# CSD-325
# Module 7 Assignment 7.2: City Functions
# This program takes a cities information and returns them in a formatted string.
# 7/13/2025

def city_country(city, country, population='', language=''):
    """Return a string in the form City, Country, with optional population and language."""
    if population and language:
        location = f"{city}, {country} - population {population}, {language}"
    elif language:
        location = f"{city}, {country}, {language}"
    elif population:
        location = f"{city}, {country} - population {population}"
    else:
        location = f"{city}, {country}"

    return location.title()


def main():
    """Main function that gets the users input to test the city_country function."""
    print("Please enter the information for a city. Press enter to skip the optional fields, and 'q' when you're ready to quit.\n")

    while True:
        city = input("City: ").lower()
        if city == "q":
            print("Thank you, good bye.")
            break
        if not city.isalpha():
            print("Please enter a valid name.")
            continue

        country = input("Country: ").lower()
        if country == "q":
            print("Thank you, good bye.")
            break
        if not country.isalpha():
            print("Please enter a valid name.")
            continue

        population = input("(Optional) Population: ")
        if population == "q":
            print("Thank you, good bye.")
            break
        elif population == "":
            population = ""
            

        language = input("(Optional) Language: ").lower()
        if language == "q":
            print("Thank you, good bye.")
            break
        elif language == "":
            language = ""
        elif not language.isalpha():
            print("Please enter a language.")
            continue


        print("Your formated location name: ", city_country(city, country, population, language))

if __name__ == '__main__':
    main()
