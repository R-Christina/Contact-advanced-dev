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
