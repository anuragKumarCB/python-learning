# Problem: Recommend a type of pet food based on the pet's species and age.
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

# take pet species
pet_species = input("Please provide your pet's species : ")
pet_species = pet_species.upper()

# take age of the pet species and convert it to integer
pet_age = input("Please provide your pet's age : ")
pet_age_in_int = int(pet_age)

# change pet into young and senior based on age
pet_is = "Young" if pet_age_in_int < 2 else "Senior"

if pet_species == "DOG":
    if pet_is == "Young":
        pet_food = "Puppy Food"
    else:
        pet_food = "Senior Dog Food"
elif pet_species == "CAT":
    if pet_is == "Young":
        pet_food = "Kitten Food"
    else:
        pet_food = "Senior Cat Food"

print(pet_food)