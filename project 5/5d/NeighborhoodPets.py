# Author: Melanie Huynh
# Date: 2/3/2021
# Description:

import json

class NeighborhoodPets:
    """
    Represents a NeighborhoodPets object which allows the user to add and delete a
    pet, search for the pet's owner, save data to a JSON file, load data from a JSON
    file, and get a set of all pet species.
    """
    def __init__(self):
        """
        Initializes NeighborhoodPets object
        """
        self._pets = {} # initializes empty json object

    def add_pet(self, pet_name, species, owner):
        """
        Takes name of a pet, the species, and the owner and adds it to the pet library
        """
        # Check to see if a pet is already in the library. If not in, add the pet
        if pet_name not in self._pets.keys():
            # add the pet using the correct parameters inputed, listed as key-value pairs
            self._pets[pet_name] = {"pet name": pet_name, "species": species, "owner": owner}

    def delete_pet(self, pet_name):
        """
        Removes a pet from the pet library
        """
        # check to see if the pet is in the library. If so, remove it
        if pet_name in self._pets.keys():
            self._pets.pop(pet_name)

    def get_owner(self, pet_name):
        """
        Returns the owner of a pet
        """
        # check to see if the pet is in the library
        if pet_name in self._pets.keys():
            return self._pets[pet_name]["owner"]

    def save_as_json(self, file_name):
        """
        Takes a file and saves it in JSON format using the input name
        """
        pets = self._pets
        with open(file_name, 'w') as outfile:
            json.dump(pets, outfile) # dumps the saved pets information into the json and saves it

    def read_json(self, file_name):
        """
        Reads and loads a file to replace all of the pets currently in memory
        """
        with open(file_name, 'r') as infile:
            self._pets = json.load(infile) # replaces the current pet information with the loaded file

    def get_all_species(self):
        """
        Returns a set of the species of all pets
        """
        species = []
        for pet in self._pets.values():
            species.append(pet["species"])
        return species

# TESTING
#np = NeighborhoodPets()
#np.add_pet("Fluffy", "gila monster", "Oksana")
#np.add_pet("Tiny", "stegasaurus", "Rachel")
#np.add_pet("Spot", "zebra", "Farrokh")

#np.save_as_json("other_pets.json")
#np.delete_pet("Tiny")
#spot_owner = np.get_owner("Spot")
#print(spot_owner)


#np.read_json("other_pets.json")  # where other_pets.json is a file it saved in some previous session
#species_set = np.get_all_species()
#print(species_set)
