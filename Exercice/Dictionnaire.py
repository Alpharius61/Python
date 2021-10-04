def main() :

    List = [

    {
        "Animals" : "Lièvre" ,
        "Colors" : "marron" ,
        "Speed" : 60,
        "Gender" : "masc",
    },
    {
        "Animals" : "Hérisson", 
        "Colors" : "gris", 
        "Speed" : 10,
        "Gender" : "masc",
    },
    {
        "Animals" : "Lapin", 
        "Colors" : "blanc", 
        "Speed" : 30,
        "Gender" : "masc",
    },
    {
        "Animals" : "Guépard", 
        "Colors" : "orange" ,
        "Speed" : 90,
        "Gender" : "masc",
    },
    {
        "Animals" : "Faucon", 
        "Colors" : "noir",
        "Speed" : 120,
        "Gender" : "masc",
    },
    {
        "Animals" : "Girafe", 
        "Colors" : "jaune", 
        "Speed" : 70,
        "Gender" : "fem",
    },
    {
        "Animals" : "Peroquet", 
        "Colors" : "bleu", 
        "Speed" : 50,
        "Gender" : "masc",
    }
    ]

    deter ="Le"
    Sprint = 0
    Slow = 10000
    printSpeed = ""

    for animalia in List :

        if animalia['Speed'] > Sprint:
            Sprint = animalia['Speed']
        
        elif animalia['Speed'] < Slow:
            Slow = animalia['Speed']


    for animalia in List :
        if animalia['Gender'] == "fem" :
            deter = "La"

        if animalia["Speed"] == Sprint :
            printSpeed = "et il est le plus rapide"
        
        elif animalia["Speed"] < Sprint :
            printSpeed =""


        if animalia["Speed"] == Slow :
            printSpeed = "et il est le plus lent"
        
        elif animalia["Speed"] < Slow :
            printSpeed =""
        

        print(f"{deter} {animalia['Animals']} {animalia['Colors']} court à {animalia['Speed']}km/h {printSpeed}")


if __name__ == "__main__" :
    main()