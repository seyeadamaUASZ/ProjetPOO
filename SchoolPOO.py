# -*- coding: UTF-8 -*-

class Personne(object):
    "classe Personne"
    def __init__(self,idP,nom,prenom,adresse,dateNaiss):
        self.idP=idP
        self.nom=nom
        self.prenom=prenom
        self.adresse=adresse
        self.dateNaiss=dateNaiss

    @property
    def identifiant(self):
        return self.idP

    @property
    def nomP(self):
        return self.nom

    @property
    def prenomP(self):
        return self.prenom

    @property 
    def dateNaissP(self):
        return self.dateNaiss

    @property
    def adresseP(self):
        return self.adresse

    @property
    def setId(self,idp):
        self.idp=idp

    @property
    def setNomP(self,nomp):
        self.nom=nomp
    
    @property
    def setPrenom(self,prenomp):
        self.prenom=prenomp

    @property
    def setAdresse(self,adressep):
        self.adresse=adressep

    @property
    def setDateNaiss(self,dateNaissp):
        self.dateNaiss=dateNaissp

    #affichage des infos d'une personne

    def __str__(self):
        return "id: {} , nom: {}, prenom: {}, adresse :{} dateNais: {}".format(self.idP,self.nom,self.prenom,self.adresse,self.dateNaiss)


#classe Enseignant

class Enseignant(Personne):
    "classe Enseignant"
    def __init__(self,idP,nom,prenom,adresse,dateNaiss,matiere="français"):
        Personne.__init__(self,idP,nom,prenom,adresse,dateNaiss)
        self.email="Ens@gmail.com"
        self.matiere=matiere

    @property
    def emailE(self):
        return self.email

    @property
    def matiereE(self):
        return self.matiere

    @property
    def setEmail(self,email):
        self.email=email

    @property
    def setMatiere(self,matiere):
        self.matiere=matiere 

    #affichage d'un enseignant

    def __str__(self):
        return "id : {}, nom: {} ,prenom: {}, email: {}, matiere: {} ".format(self.idP,self.nom,self.prenom,self.email,self.matiere)

#classe eleve

class Eleve(Personne):
    "classe Eleve..."

    def __init__(self,idP,nom,prenom,adresse,dateNaiss):
        Personne.__init__(self,idP,nom,prenom,adresse,dateNaiss)
    
    #affichage d'un eleve
    def __str__(self):
        return "nom:{}, prenom: {}, adresse: {}, dateNaiss:{}".format(self.nom,self.prenom,self.adresse,self.dateNaiss)

    #calculer sa moyenne à partir des arguments de notes  tuplé

    def calculmoyenne(self,*args):
        somme=0
        for i in args:
            somme+=i
        return float(somme/len(args))

#on définit la classe Classe avec des élèves et un enseignant

class Classe(object):
    "classe Classe"
    
    def __init__(self,nomClasse,enseignant):
        self.nomClasse=nomClasse
        self.enseignant=enseignant
        self.eleves=[]
        

    #ajouter un éleve à la liste
    
    def ajouter(self,elev):
        self.eleves.append(elev)
        return "ok"
        
    @property
    def leseleves(self):
        for i in range(len(self.eleves)):
            if(self.eleves==None):
                print("pas d'élèves")
            else:
                print(self.eleves[i].nomP," ",self.eleves[i].prenomP)
            


    
    #affichage d'une classe

    def __str__(self):
        return "nom de la classe: {} avec comme enseignant : {} {}".format(self.nomClasse,self.enseignant.nom,self.enseignant.prenom)



#programme principal

if __name__=="__main__":
    personne=Personne(1,"seye","Adama","sikilo","28/10/1993")
    personne2=Personne(2,"Gueye","ana","tilene","15/01/1998")
    print(personne)
    print(personne2)
    print("******information Enseignant*********")
    ens=Enseignant(1,"diallo","henry","sikilo","15/03/1993","anglais")
    print(ens)
    print("*******information Eleve********")
    elev=Eleve(1,"Ndiaye","Anna","Medina Gounass","27/03/1994")
    elev2=Eleve(2,"Samba","ibou","Medina Gounass","27/03/1997")
    print(elev)
    print(elev2)

    print()

    print("*****Calcul Moyenne******")

    print("la moyenne de l'eleve id: ",elev.identifiant,"de nom ",elev.nomP , elev.prenomP," est de : ",elev.calculmoyenne(15,12,13,11))

    #une classe
    classe=Classe("ci",ens)
    print(classe)

    print("*****les eleves de la classe****")
    print(classe.ajouter(elev))
    print(classe.ajouter(elev2))


    classe.leseleves

    


 



