# coding : utf-8

import  time

def main ():
    #Loops ()
    Lists ()
    #StringList ()


def Loops ():
   
    maxNumber = 100
    number = int(input ("Nombre de départ : " ))


    print ("Début boucle while")
    while (number <= maxNumber) :
        
        print (number)
        number += 3 # incrémentation 
    print ("Terminé")

    number = int(input ("Nombre de départ : " ))
    print ("Début boucle for")
    for number in range (number, maxNumber, 3) :

        print (number)
        number += 1
    print ("Terminé")


def Lists () :
 Numbers = [0,1,2,3,4,5,6,7,8,9]
 Names = ["Gaël", "Théo", "Cécilia", "Timothée"]
 MyList = ["Alain", 35, False, 28] # On peut mélanger la nature des élément de la liste en python....déconseillé
 
 # print element in Numbers with in
 for Element in Numbers :
     print (Element)
 
 print ("\n\n")

 # print element in Numbers with index
 myList = Numbers
 for Index in range ((len(myList))):
     print (myList[Index])

 # print element at a range 
 print (Names[2])

 #add elements to list
 NewPerson = None
 while NewPerson !== "":
 NewPerson = input ("Entrer votre nom : ")
 if NewPerson != "" :
     Names.append(NewPerson)
 for  Element in Names:
     print(Element)




def StringList () :
    name = "Sauron y a laissé les doigt"
    speed = 0.02
    for Element in name :
        # if (Element == "o" or Element == "e") :
        #     pass
        # else :
        #     print(Element, end = "")

        # if(no(Element == "o" or Element == "e")) :
        #     print(Element, end="")

        if (Element == "o" or Element == "e") :
            continue
        print(Element, end="", flush=True)
        time.sleep(speed)



if __name__ == "__main__" :
    main()
