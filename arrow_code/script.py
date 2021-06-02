from dataclasses import dataclass

@dataclass
class User:
    name: str
    is_active: bool
    is_foreign: bool
    language : str
    age: int

    def say_hello(self, message):
        print(message)


def international_hello(self, user: User, language: str):

    colleagues = ["Manolo", "Cherryl", "Luigi"]

    for colleague in colleagues:
        if language == "spanish":
            if user.age > 18 and user.age < 25:
                if user.is_active:
                    if user.is_foreign:
                        message = "hola" + " " + colleague
                        user.say_hello(message)
                    else:
                        message = "hi" + " " + colleague
                        user.say_hello(message)
                
                else:
                    print("Inactive user")
            else:
                print("You can not be my colleague")
        elif language == "english":
            if user.age > 18 and user.age < 25:
                if user.is_active:
                    if user.is_foreign:
                        message = "hi" + " " + colleague
                        user.say_hello(message)
                    else:
                        message = "hola" + " " + colleague
                        user.say_hello(message)
                else:
                    print("Inactive user")
            else:
                print("You can not be my colleague")
        elif language == "italian":
            if user.age > 18 and user.age < 25:
                if user.is_active:
                    if user.is_foreign:
                        message = "Ciao" + " " + colleague
                        user.say_hello(message)
                    else:
                        message = "hi" + " " + colleague
                        user.say_hello(message)
                else:
                    print("Inactive user")
            else:
                print("You can not be my colleague")
        else:
            print("Language not found")
        
        

