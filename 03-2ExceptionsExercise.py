class Person:
    def __init__(self, name: str):
        try:
            if any(char.isdigit() for char in name) and name.isupper():
                self.name = name
        except Exception as ex:
            print(f"an error occured: {ex}")


valid_person = Person("Frederik")
invalid_person = Person("1233fhasdasf")
