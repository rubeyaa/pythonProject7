#créé en 2023
#Créé par Adam Rubeya
#POO num 2
import random
def dé():
    de1 = random.randint(1,6)
    de2 = random.randint(1,6)
    de3 = random.randint(1,6)
    de4 = random.randint(1,6)
    if de1 <= de2 and de1 <= de3 and de1 <= de4:
        return de2+de3+de4
    elif de2 <= de1 and de2 <= de3 and de2 <= de4:
        return de1+de3+de4
    elif de3 <= de1 and de3 <= de2 and de3 <= de4:
        return de1+de2+de4

class NPC:
    def __init__(self):
        self.pv = dé(1, 20)
        self.nom = "Loris"
        self.race = "Atlas"
        self.espece = "Sirène"
        self.classearmure = random.randint(1, 12)
        self.force = dé()
        self.agilité = dé()
        self.constitution = dé()
        self.intelligence = dé()
        self.sagesse = dé()
        self.charisme = dé()
        self.profession = "Guerrière"

class Héros(NPC):
    def __init__(self):
        self.nom = "Hiras"
        self.race = "Atlas"
        self.espece = "Sirène"
        self.profession = "guerrier"
    def attaquer(self, cible):
        npc.subir(random.randint(1,6))
        de = random.randint(1, 20)
        de8 = random.randint(1,8)
        if de == 1:
            print("vous avez échouez.")
        elif de == 20:
            print("votre attaque a réussi")
            cible.subir(random.randint(1,8))
            def subir(self, dommage):
                self.pv -= dommage
        elif de ==[2,19]:
            if de < self.classearmure:
                print("vous avez échoué")
            elif de > self.classearmure:
                print("vous avez réussi")
                cible.subir(random.randint(1,6))
    def subir(self, dommage):
        self.pv -= dommage




    def subir(self, dommage):
        self.pv -= dommage


class KOBOLD(NPC):
    def __init__(self):
        self.pv - dé()
        self.nom = "Brak"
        self.race = "Kobold"
    def attaquer(self):
        npc.subir(random(1,6))
    def subir(self, dommage):
        self.pv -=dommage


npc = NPC()
kobold = KOBOLD()
print(kobold.nom)

npc = NPC()
print(npc.pv ,"\n",npc.nom ,"\n",npc.race ,"\n",npc.espece ,"\n",npc.classearmure ,"\n",npc.force ,"\n",npc.agilité ,"\n",npc.constitution ,"\n",npc.intelligence ,"\n",npc.sagesse ,"\n",npc.charisme ,"\n",npc.profession)
