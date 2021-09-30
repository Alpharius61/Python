def main():
    example = ['hello', 'good morning', 'bye bye', 'have a good day']
    placeOfChange = int(input("Choose the position of the element that you want change : "))
    Change = input("What you want place : ")
    example[placeOfChange-1] = Change
    print(example)


if __name__=="__main__" :
    main()