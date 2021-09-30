def main () :
    print("Bonjour")
    annéeActuelle = 2021
    nbPersonne = int(input ("Combien y a t'il de personne ? \n"))
    for i in range (nbPersonne):
        name = input ("Quels est ton noms ? ")
        age = int(input ("Quel est ton age ? "))
        annéeNaissance = annéeActuelle - age
        print (f"Tu es {name}, tu as {age} ans et tu es née en {annéeNaissance}")

main()