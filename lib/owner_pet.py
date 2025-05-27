class Pet:
    
    PET_TYPES =  ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.pet_type = pet_type
        if owner is not None:
            if isinstance(owner, Owner):
                self.owner = owner
            else:
                raise Exception("Owner must be an instance of Owner")
        else:
            self.owner = None
        Pet.all.append(self)
        
        
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self,pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("Invalid pet type")
        
        
class Owner:
    def __init__(self,name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self,pet):
        if not isinstance(pet, Pet):
            raise Exception("Can only add Pet instances")
        pet.owner = self
    
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)