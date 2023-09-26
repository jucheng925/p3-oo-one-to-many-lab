class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner = None):
        self.name = name
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Pet type need to be in pet_types list")
        self.owner = owner
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(Pet.all, key =lambda p:p.name)
