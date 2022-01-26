class player:
    def __init__(self,nom,chanson1,chanson2,chanson3,chanson4,chanson5):
        self.__nom = nom
        self.__score = (chanson1,chanson2,chanson3,chanson4,chanson5)
        self.__score2 =2
        self.__score3 =1
        self.__score4 =3
        self.__score5 =4
    def getBestScore(self,__score): ## affiche meileeur score et chanson
        bestscore="0"
        chanson=-1
        for i in range(__score):
            if __score[i] > bestscore:
                bestscore = __score[i]
        for i in range(__score):
            if __score[i] == bestscore:
                chanson = i
        print (bestscore)
        print ("chanson",chanson)
        return bestscore
    
    def getMoyenneScore (self,__score): ## affiche et calcule la moyenne des score
        moyenne=0
        for i in range(__score):
            moyenne +=__score[i]
        moyenne = moyenne/5
        print(moyenne)
        return moyenne 
    
    def getPireScore (self,__score):
        pirfescore=100
        for i in range(__score):
            if __score[i] < pirfescore:
                pirfescore = __score [i]
        print("pire score = ",pirfescore)
        return pirfescore
    
    def affichescore(self,__score):
        for i in range(__score):
            print (__score[i])
            
    def getscore(self,__score):
        return __score
                    
    def newScore(self,__score):
        chansonModif = int(input("Quel score modifier \n"))
        scoremodif = int(input("Quel est le nouveau score \n"))
        for i in range(__score):
             if i == chansonModif:
                __score[i] = scoremodif

shalcon = player ("shalcon",50,60,0,95,80)

shalcon.getBestScore(shalcon.getscore())
shalcon.getMoyenneScore(shalcon.getscore())
shalcon.getPireScore(shalcon.getscore())
shalcon.getscore(shalcon.getscore())
shalcon.newScore(shalcon.getscore())



