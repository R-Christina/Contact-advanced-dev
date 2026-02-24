from services.ServiceContact import ServiceContact

def main():
    service = ServiceContact()
    while True:
        print("\n--- Gestion des contacts ---")
        print("1. Ajouter un contact")
        print("2. Afficher les contacts")
        print("3. Supprimer un contact")
        print("4. Vérifier si un numéro existe déjà")
        print("5. Voir le nombre total de contacts")
        print("6. Modifier un contact")
        print("7. Quitter")
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
                nom = input("Nom du contact à supprimer : ")
                service.delete_contacts(nom)
                print("Contact supprimé !")
            case "4":
                numero = input("Numéro à vérifier : ")
                if service.verify_numero_exist(numero):
                    print("Le numéro existe déjà.")
                else:
                    print("Le numéro n'existe pas.")
            case "5":
                print(f"Nombre total de contacts : {service.count_contacts()}")
            case "6":
                nom = input("Nom du contact à modifier : ")
                new_nom = input("Nouveau nom (laisser vide si inchangé) : ") or None
                new_numero = input("Nouveau numéro (laisser vide si inchangé) : ") or None
                service.modify_contact(nom, new_nom=new_nom, new_numero=new_numero)
            case "7":
                print("Au revoir !")
                break
            case _:
                print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()