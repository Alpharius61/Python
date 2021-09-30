def main() :

    Word = input("Choose your word : ")
    ChangeChar = input("Choose the character you want to change : ")
    NewChar = input("Choose the new characters : ")
   
    for i in range (len(Word)) :
        if Word[i] == ChangeChar :
            print(NewChar, end="")
        else :
            print(Word[i], end="")
    

if __name__ == "__main__" :
    main()