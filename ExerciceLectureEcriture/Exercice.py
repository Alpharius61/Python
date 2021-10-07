
import Data.Variable as Var
import os.path


def main():
    Choose()



def Choose():
    UserInput = ""
    while UserInput != "Q":
        UserInput = input(
            """
            Que veux-tu faire ?
            (A)fficher la liste des personnes
            A(j)outter une personne
            A(d)d points
            (S)auvegarder la liste dans un fichier
            (C)harger la liste depuis un fichier
            (Q)uitter
            Choix : """).upper()
        
        print()

        if UserInput == "Q":
            print("Au revoir\n")

        elif UserInput == "A":
            SeePerson()
            print()

        elif UserInput == "J":
            NewPerson()
            print()

        elif UserInput == "S":
            SavePerson()

        elif UserInput == "C":
            LoadPerson()

        elif UserInput =='D' :
             AddPoint()

def SeePerson():
    for Person in Var.Persons :
        
        print(f"""{Person['FirstName']}, {Person['Surname']} is {Person['Age']} years.\nIt's a {Person['Gender']} and has {Person['Score']} points """)
        

def NewPerson() :
    print("""Enter the Firstname, Surname, the age, the gender (boy or girl) 
    and the score of the new person separated by ',' : \n """)
    
    NP = input("Nouvelle personne : ")
    PersonData = NP.split(",")

    try :
        Var.Persons.append(
            { 
                
                "FirstName" : PersonData[0],
                "Surname" : PersonData[1],
                "Age" : int(PersonData[2]),
                "Gender" : PersonData[3],
                "Score" : int(PersonData[4]),
            }
            
        )
        print(f"\nPerson add to list") 

    except ValueError:
        print("\nThe age is not number !")
    except IndexError:
        print("\nInformations are missing !")


def AddPoint ():
    FirstNamePlayer = input("Wich person will have points ?")
    PersonPoint = int(input(f"Choose points wich have the person"))
     
    for Person in Var.Persons : 
         if Person["FirstName"] == FirstNamePlayer:
             Person['Score'] = PersonPoint
    print(f"{FirstNamePlayer} has {PersonPoint}")



def SavePerson() :
    with open("Data/Variable.txt", "w", encoding="utf-8") as MyFile:
        # for each Persons il list
        for Persons in Var.Persons:
            # create temporary list of Persons data
            PersonData = []
            # for each data in Persons (dictionary)
            for Value in Persons.values():
                # add persons data to temporary list
                PersonData.append(str(Value))
            # write list strings separated with , to file
            MyFile.write(f"{','.join(PersonData)}\n")

    print("Folder saved")


def LoadPerson() :
 # reset list
    Var.Persons = []

    # open file MyFile in read mode
    with open("Variable.txt", "r", encoding="utf-8") as MyFile:
        # load each file line in PersonData list
        PersonData = MyFile.readlines()
        # for each Persons in list
        for Person in PersonData:
            # split Persons data with , as separator
            PersonData = Person.split(",")
            # add new Persons as dictionary to Persons list
            Var.Persons.append(
                {
                    "FirstName" : PersonData[0],
                    "Surname" : PersonData[1],
                    "Age" : int(PersonData[2]),
                    "Gender" : PersonData[3],
                    "Score" : int(PersonData[4]),
                }
            )

    print("Folder loaded")






if __name__=="__main__":
    main()
