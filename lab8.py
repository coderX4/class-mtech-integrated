class String:
    def __init__(self):
        self.vowel=0
        self.uppercase=0
        self.lowercase=0
        self.consonants=0
        self.space=0
        self.string=input("Enter the string: ")
    def count_uppercase(self):
        for i in self.string:
            if i.isupper():
                self.uppercase+=1

    def count_lowercase(self):
        for i in self.string:
            if i.islower():
                self.lowercase += 1

    def count_vowel(self):
        for i in self.string:
            if i in ('a','e','i','o','u'):
                self.vowel += 1
            elif i in ('A','E','I','O','U'):
                self.vowel+=1

    def count_consonants(self):
        for i in self.string:
            if i in ('a','e','i','o','u'):
                pass
            else:
                self.consonants+=1
    def count_space(self):
        for i in self.string:
            if i == " ":
                self.space += 1
    def compute(self):
        self.count_space()
        self.count_consonants()
        self.count_uppercase()
        self.count_lowercase()
        self.count_vowel()
    def display(self):
        print("Vowel: ",self.vowel)
        print("Consonants: ",self.consonants)
        print("Spaces: ",self.space)
        print("Lowercase :",self.lowercase)
        print("Uppercase :",self.uppercase)
s=String()
s.compute()
s.display()

