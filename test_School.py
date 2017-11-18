import SchoolPOO
import pytest

class Test_School():
    personne=SchoolPOO.Personne(1,"samba","Diallo","sikilo","28/02/1998")
    elev=SchoolPOO.Eleve(1,"samba","Diallo","sikilo","28/02/1998")
    def test_nom(self):
        assert self.personne.nom=="samba"

    def test_prenom(self):
        assert self.personne.prenom=="Diallo"

    def test_nomel(self):
        assert self.elev.adresse=="sikilo"

    def test_moyenne(self):
        assert self.elev.calculmoyenne(15,12,13,11)==12.75

    
