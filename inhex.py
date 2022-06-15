class Animal:  
    def speak(self):  
        print("Animal Speaking")    
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak() 




class Animal:  
    def speak(self):  
        print("Animal Speaking")  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
class DogChild(Dog):  
    def eat(self):  
        print("Eating bread...")  
obj= DogChild()  
obj.bark()  
obj.speak()  
obj.eat()  


