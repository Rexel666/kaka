def calculer_calories(sexe, age, poids, taille, niveau_activite):
    if sexe.lower() == 'homme':
        bmr = 88.362 + (13.397 * poids) + (4.799 * taille) - (5.677 * age)
    elif sexe.lower() == 'femme':
        bmr = 447.593 + (9.247 * poids) + (3.098 * taille) - (4.330 * age)
    else:
        return "Sexe non reconnu. Veuillez entrer 'homme' ou 'femme'."

    niveaux = {
        '1': 1.2,  # Sédentaire
        '2': 1.375,  # Légèrement actif
        '3': 1.55,  # Modérément actif
        '4': 1.725,  # Très actif
        '5': 1.9  # Extrêmement actif
    }

    if niveau_activite in niveaux:
        return bmr * niveaux[niveau_activite]
    else:
        return "Niveau d'activité non reconnu. Veuillez choisir entre 1 et 5."

def main():
    print("Calculateur de calories quotidiennes")
    sexe = input("Entrez votre sexe (homme/femme): ")
    age = int(input("Entrez votre âge: "))
    poids = float(input("Entrez votre poids en kg: "))
    taille = float(input("Entrez votre taille en cm: "))
    print("Niveaux d'activité:")
    print("1. Sédentaire")
    print("2. Légèrement actif")
    print("3. Modérément actif")
    print("4. Très actif")
    print("5. Extrêmement actif")
    niveau_activite = input("Choisissez votre niveau d'activité (1-5): ")

    calories = calculer_calories(sexe, age, poids, taille, niveau_activite)
    if isinstance(calories, str):
        print(calories)
    else:
        print(f"Vos besoins caloriques quotidiens estimés sont de {calories:.2f} calories.")

if __name__ == "__main__":
    main()
