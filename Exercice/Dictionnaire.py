List = [

{
    "Animals" : "Lièvre" ,
    "Couleur" : "marron" ,
    "Vitesse" : 60,
    "Genre" : "masc",
},
{
    "Animals" : "Hérisson", 
    "Couleur" : "gris", 
    "Vitesse" : 10,
    "Genre" : "masc",
},
{
    "Animals" : "Lapin", 
    "Couleur" : "blanc", 
    "Vitesse" : 30,
    "Genre" : "masc",
},
{
    "Animals" : "Guépard", 
    "Couleur" : "orange" ,
    "Vitesse" : 90,
    "Genre" : "masc",
},
{
    "Animals" : "Faucon", 
    "Couleur" : "noir",
    "Vitesse" : 120,
    "Genre" : "masc",
},
{
    "Animals" : "Girafe", 
    "Couleur" : "jaune", 
    "Vitesse" : 70,
    "Genre" : "fem",
},
{
    "Animals" : "Peroquet", 
    "Couleur" : "bleu", 
    "Vitesse" : 50,
    "Genre" : "masc",
}
]

deter ="Le"
Sprint = 0
Lent = 10000
printSpeed = ""



for animalia in List :

    if animalia['Vitesse'] > Sprint:
        Sprint = animalia['Vitesse']
    
    elif animalia['Vitesse'] < Lent:
        Lent = animalia['Vitesse']


for animalia in List :
    if animalia['Genre'] == "fem" :
        deter = "La"

    if animalia["Vitesse"] == Sprint :
        printSpeed = "et il est le plus rapide"
    
    elif animalia["Vitesse"] < Sprint :
        printSpeed =""


    if animalia["Vitesse"] == Lent :
        printSpeed = "et il est le plus lent"
    
    elif animalia["Vitesse"] < Lent :
        printSpeed =""
    

    print(f"{deter} {animalia['Animals']} {animalia['Couleur']} court à {animalia['Vitesse']}km/h {printSpeed}")