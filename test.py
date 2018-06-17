class Person:
    def __init___(self, name, age):
        self.name = name
        self.age = age

    def ask_name(self):
        self.name = raw_input("What's your name?")

    def ask_age(self):
        while True:
            try:
                self.age = int(raw_input("What's your age?"))
                break # we managd to get a correct input, exit the loop
            except ValueError:
                print("Enter a valid number.")
                #better try again... Return to the start of the loop
                continue

    def print_name(self):
        print("Hi {}".format(self.name))

    def print_age(self):
        print("You're {} years old".format(self.age))

    def introduce(self):
        self.print_name()
        self.print_age()

def main():
    p = Person()

    p.ask_name()
    p.ask_age()
    
    p.introduce()    
        
    temp = raw_input() #Leave this here. Needed to pause the program

main()
