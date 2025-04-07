# Speed of light in meters per second (constant)
C: int = 299792458

# Define the main function where the core logic of the program resides
def main():
    # Display a welcome message to the user
    print("Welcome to the Energy-Mass Equivalence Calculator (E = mc²)!")

    # Get the mass input from the user and convert it to a float
    mass_in_kg: float = float(input("Enter the Mass in KG: "))
    
    # Display the formula and values used in the calculation
    print("E = m * C²...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    
    # Calculate the energy using the formula E = mc²
    energy_in_joules: float = mass_in_kg * (C ** 2)

    
    # Print the calculated energy in joules
    print(f"The energy equivalent of {mass_in_kg} kg is {energy_in_joules} joules.")

# This condition ensures that the main() function will run
# only when this script is executed directly (not when imported as a module)
if __name__ == '__main__':
    main()
