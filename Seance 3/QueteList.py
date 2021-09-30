
def main() :
    
    List = []
    
    
    NbElement = int(input("Nombre d'élément dans la list : "))
    
    
    
    for i in range (0,NbElement) :
        Temp1 = int(input("Saisir un nobmre : "))
        List.append(Temp1)

    List.sort()
    
    print(List)

if __name__ == "__main__" :
    main()