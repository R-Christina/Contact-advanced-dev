from services.ServiceContact import ServiceContact

def main():
	service = ServiceContact()
	while True:
		print("\n--- Gestion des contacts ---")
		print("1. Ajouter un contact")
		print("2. Afficher les contacts")
		print("3. Quitter")
		choice = input("Choisissez une option : ")

		match choice:
			case "1":
				nom = input("Nom : ")
				numero = input("Numéro : ")
				service.add_contact(nom, numero)
				print("Contact ajouté !")
			case "2":
				service.show_contacts()
			case "3":
				print("Au revoir !")
				break
			case _:
				print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
	main()