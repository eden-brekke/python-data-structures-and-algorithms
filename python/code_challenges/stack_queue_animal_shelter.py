from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()

    def enqueue(self, animal):
        if isinstance(animal, Cat):
            self.cats.enqueue(animal)
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        else:
            return "Sorry that's not a cat or a dog, let's get you in contact with a shelter that can help you!"

    def dequeue(self, pref):
        if pref == "cat" and self.cats:
            return self.cats.dequeue()
        if pref == "dog" and self.dogs:
            return self.dogs.dequeue()
        else:
            return None


class Dog:
    pass


class Cat:
    pass
