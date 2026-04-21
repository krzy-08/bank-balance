import json

FILE_NAME = "contact.json"

def load_contact():
    try:
        with open (FILE_NAME, "r") as f:
            data = json.load(f)
            contacts = {}
            for name, info in data.items():
                contacts[name] = Contact(info["name"], info["phone"])
            return contacts
    except FileNotFoundError:
        return {}


class Contact():
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Name: {self.name} | Phone: {self.phone}")
    
    def validate(self):
        return self.phone.isdigit()
    
    def to_dict(self):
        return {"name": self.name, "phone": self.phone}
    


john = Contact("John", "0948296")
athena = Contact("Athena", "0951450")
eloise = Contact("Eloise", "John")

data = {
    "John": john.to_dict(),
    "Athena": athena.to_dict(),
    "Eloise": eloise.to_dict()
}

json.dump(data, open(FILE_NAME, "w"))
more_data = load_contact()

for name, info in more_data.items():
    info.display()
