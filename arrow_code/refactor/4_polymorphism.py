from dataclasses import dataclass

@dataclass
class User:
    name: str
    is_active: bool
    is_foreign: bool
    language : str

    def say_hello(self, name):
        print(f"Hi {name}")

    # Decompose conditional in methods
    def validate_user(self):
        accepted_age = range(18, 25)

        if not self.age in accepted_age:
            raise ValueError("You can not be my colleague")

        if not self.is_active:
            raise ValueError("Inactive user")

# Polymorphism
class SpanishUser(User):
    def say_hello(self, name):
        print(f"Hola {name}")

class ItalianUser(User):
    def say_hello(self, name):
        print(f"Ciao {name}")

class FactoryUser:
    def __init__(self):
        self.languages = {
            "spanish": SpanishUser(),
            "english": User(),
            "italian": ItalianUser()
        }

    def get_user_type(self, language) -> User:
        try:
            return self.languages[language]
        except KeyError:
            raise ValueError("Language not found")


def international_hello(self, user: User, language: str):
    colleagues = ["Manolo", "Cherryl", "Luigi"]

    # Call decompose method
    user.validate_user()

    factory = FactoryUser()
    
    for colleague in colleagues:
        # Polymorphism
        user_to_send_message = factory.get_user_type(language)
        user_to_send_message.say_hello(colleague)