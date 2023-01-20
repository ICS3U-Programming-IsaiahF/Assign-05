#!/usr/bin/env python3

# Created by: Isaiah Fernandez
# Date: January 11, 2023
# This program allows the user to enter a mass of something then it calculates the energy of that thing.

# This function converts mass to energy
def e_mc_squared(mass, unit):
    # Speed of light constant
    speed_light = 2.99792 * 10 ** 8  # m/s
    # Calculate energy at rest
    energy = (mass * speed_light ** 2)
    # Convert energy to selected unit
    if unit == "joules":
        energy = energy
    elif unit == "kilojoules":
        energy = energy / 1000
    elif unit == "megajoules":
        energy = energy / 1000000
    elif unit == "kilocalories":
        energy = energy / 4184
    elif unit == "watts":
        energy = energy / 1
    elif unit == "kilowatts":
        energy = energy / 1000
    elif unit == "megawatts":
        energy = energy / 1000000
    elif unit == "gigawatts":
        energy = energy / 1000000000
    elif unit == "terawatts":
        energy = energy / 1000000000000
    elif unit == "watt hours":
        energy = energy / 3600
    elif unit == "kilowatt hours":
        energy = energy / 3600000
    elif unit == "megawatt hours":
        energy = energy / 3600000000
    elif unit == "gigawatt hours":
        energy = energy / 3600000000000
    elif unit == "terawatt hours":
        energy = energy / 3600000000000000
    else:
        print("Invalid unit selected")
        
    
    return energy

#This function gets user input for mass and displays energy
def main():
    # Ask user for mass and checks if user number is a number
    print("")
    try: 
        mass = float(input("Enter the mass (in kilograms): "))
        print("")

    except ValueError:
        print("")
        print("Please input a number")
        print("")
        return main()
    # Checks if the mass entered by user is negative, if so asks them to input a positive number
    if mass < 0:
        print("Please enter a positive number")
        print("")
        return main()
    
    # Ask user for unit of measurement
    valid_units = ["joules", "kilojoules", "megajoules", "Kilocalories", "watts", 
               "Kilowatts", "Megawatts", "Gigawatts", "Terawatts", "Watt hours", 
               "Kilowatt hours", "Megawatt hours", "Gigawatt hours", "Terawatt hours"]
    unit = input("Select unit of measurement (joules, kilojoules, megajoules, Kilocalories, watts, \
                 Kilowatts, Megawatts, Gigawatts, Terawatts, Watt hours, \
                 Kilowatt hours, Megawatt hours, Gigawatt hours, Terawatt hours): ")
    if unit not in valid_units:
        print("Please enter a valid unit")
        print("")
        return main()
    # Calls the E=mc squared function with the users mass and selected unit
    energy = e_mc_squared(mass, unit)
    # Display the results
    print("")
    print("The amount of energy at rest is: {:.2f} {}".format(energy, unit))
    print("")

if __name__ == "__main__":
    main()