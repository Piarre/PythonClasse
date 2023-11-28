
def main():
    total = 0
    effTotal = 0
    note = int(input("Combien de notes : "))

    for i in range(note):
        try:
            notesInEff = int(input(f"Combien de notes pour l'effectif {i+1} : "))
        except:
            print("Erreur, veuillez recommencer")
            notesInEff = int(input(f"Combien de notes pour l'effectif {i+1} : "))
        
        try:
            eff = int(input(f"Combien d'effectif pour la note {i+1} : "))
        except:
            print("Erreur, veuillez recommencer")
            eff = int(input(f"Combien d'effectif pour la note {i+1} : "))

        total += (eff * notesInEff)
        effTotal += eff
        print("\n")

    print(total / effTotal)
    # print(((3*2) + (5*3) + (6*3) + (7*4) + (8*2) + (10*1)) / (2+3+3+4+2+1))

main()

# 5.53
