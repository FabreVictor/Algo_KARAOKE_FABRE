class player:
    def __init__(self,nom,chanson1,chanson2,chanson3,chanson4,chanson5):
        self.__nom = nom
        self.__score = (chanson1,chanson2,chanson3,chanson4,chanson5)

    def getBestScore(self,): ## affiche meileeur score et chanson
        bestscore="0"
        chanson=-1
        for i in range(self.__score):
            if self.__score[i] > bestscore:
                bestscore = self.__score[i]
        for i in range(self.__score):
            if self.__score[i] == bestscore:
                chanson = i
        print (bestscore)
        print ("chanson",chanson)
        return bestscore
    
    def getMoyenneScore (self): ## affiche et calcule la moyenne des score
        moyenne=0
        for i in range(self.__score):
            moyenne +=self.__score[i]
        moyenne = moyenne/5
        print(moyenne)
        return moyenne 
    
    def getPireScore (self):
        pirfescore=100
        for i in range(self.__score):
            if self.__score[i] < pirfescore:
                pirfescore = self.__score [i]
        print("pire score = ",pirfescore)
        return pirfescore
    
    def affichescore(self):
        for i in range(self.__score):
            print (self.__score[i])
            
    def getscore(self):
        return self.__score
                    
    def newScore(self):
        chansonModif = int(input("Quel score modifier \n"))
        scoremodif = int(input("Quel est le nouveau score \n"))
        for i in range(self.__score):
             if i == chansonModif:
                self.__score[i] = scoremodif

shalcon = player ("shalcon",50,60,0,95,80)

shalcon.getBestScore()
shalcon.getMoyenneScore()
shalcon.getPireScore()
shalcon.getscore()
shalcon.newScore()



class karaoke:
    def __init__(self,):
        self.fuck
