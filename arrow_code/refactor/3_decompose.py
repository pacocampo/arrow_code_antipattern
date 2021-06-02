from dataclasses import dataclass

@dataclass
class User:
    name: str
    is_active: bool
    is_foreign: bool
    language : str

    def say_hello(self, message):
        print(message)

    # Decompose conditional in methods
    def validate_user(self):
        accepted_age = range(18, 25)

        if not self.age in accepted_age:
            raise ValueError("You can not be my colleague")

        if not self.is_active:
            raise ValueError("Inactive user")


def international_hello(self, user: User, language: str):
    available_languages = ["spanish", "english", "italian"]
    colleagues = ["Manolo", "Cherryl", "Luigi"]

    # Call decompose method
    user.validate_user()

    #Guard Clause for language not found
    if language not in available_languages:
        print("Language not Found")

    for colleague in colleagues:
        #Guard Clause for is_foreign user
        if not user.is_foreign:
            greeting = "hi"

        if language == "spanish":    
            greeting = "hola"
        if language == "english":
            greeting = "hi"
        if language == "italian":
            greeting = "hi"
        
        # Consolidate duplicades
        user.say_hello(f"{greeting} {colleague}")