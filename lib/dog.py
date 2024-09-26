class Dog:
    approved_breeds = ["Pug", "Bulldog", "Beagle", "Labrador"]

    def __init__(self, name="", breed=""):
        self._name = None
        self._breed = None
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = name.title()

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        # Stop execution if name is invalid to avoid printing breed error
        if not self._name:
            return
        if breed not in Dog.approved_breeds:
            print("Breed must be in list of approved breeds.")
            return
        self._breed = breed
