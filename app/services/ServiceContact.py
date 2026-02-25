from models.Contact import Contact


class ServiceContact:
    def __init__(self):
        self.contacts = []

    def add_contact(self, nom, numero):
        contact = Contact(nom, numero)
        self.contacts.append(contact)

    def show_contacts(self):
        if not self.contacts:
            print("Aucun contact enregistré.")
        else:
            print("Liste des contacts :")
            for idx, contact in enumerate(self.contacts, 1):
                print(f"{idx}. {contact.nom} - {contact.numero}")

    def delete_contacts(self, nom):
        for contact in self.contacts:
            if contact.nom == nom:
                self.contacts.remove(contact)
                return
        print("Contact non trouvé.")

    def verify_numero_exist(self, numero):
        for contact in self.contacts:
            if contact.numero == numero:
                return True
        return False

    def count_contacts(self):
        return len(self.contacts)


