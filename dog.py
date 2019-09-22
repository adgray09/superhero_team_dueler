class Dog:
    def  __init__ (self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")


my_dog = Dog("Romeo", "Greyhound")
print(my_dog)
my_dog.bark()
print(my_dog.name)
print(my_dog.breed)
