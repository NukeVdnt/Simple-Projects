#game adopts some idea from the pokemon games all the stats and information are hypothetical
import random
import time
print(" ______   _____    ___   ____  __    __   _____   __   __             ")
time.sleep(0.5)
print("|______| |     | |/     |____  | \__/ |  |     |  | \  |      ")
time.sleep(0.5)
print("|        |_____| |\___  |____  |      |  |_____|  |  \_|           ")
time.sleep(0.5)
print()
print(" ______   _____  _______ _       _        _____              ")
time.sleep(0.5)
print("|______| |_____|    |    |       |       |_____      ")
time.sleep(0.5)
print("|______| |     |    |    |_____  |_____  |_____      ")
time.sleep(0.5)
print()
print(" ______    _____    _____  _     _  __   _  ______   _____      ")
time.sleep(0.5)
print("|      _  |_____|  |     | |     |  | \  |  |     | |_____    ")
time.sleep(0.5)
print("|______|  |\_____  |_____| |_____|  |  \_|  |_____| ______|            ")
time.sleep(0.5)
print()
print()
userName=input("please enter your name: ")
print()
print()
print("WELCOME TO THE POKEMON BATTLE GROUNDS, "+userName)
print()
print()
class Pokemon:
    def __init__(self,name,pokeType,normalAttack,specialAttack,health=200):
        self.name=name
        self.pokeType=pokeType
        self.normalAttack=normalAttack
        self.specialAttack=specialAttack
        self.health=health
pokemon1=Pokemon("pikachu","electric","lightning ball","thunderstorm")
pokemon2=Pokemon("charizard","fire","smoky breath","fire storm")
pokemon3=Pokemon("gengar","poison","dark matter","ghost ghoul")
pokemon4=Pokemon("arcanine","fire","sonic blast","wild fire")
pokemon5=Pokemon("bulbasaur","grass","leaf blast","unleash")
pokemon6=Pokemon("blaziken","fire","fire arms","equalize")
pokemon7=Pokemon("umbreon","dark","stalk","silent killer")
pokemon8=Pokemon("lucario","steel","anticipate","aura drain")
pokemon9=Pokemon("gardevoir","psychic","mind burst","psychokinetic pool")
pokemon10=Pokemon("eevee","normal","trickster","transform")
pokemon11=Pokemon("dragonite","fire","sonic fist","inferno whirlpool")
pokemon12=Pokemon("absol","dark","calmity","disaster management")
pokemon13=Pokemon("typholsion","fire","fire fist","volcano")
pokemon14=Pokemon("ampharos","electric","daze","to space")
pokemon15=Pokemon("squirtle","water","ultra water blast","iron shield")
pokemon16=Pokemon("flygon","garden","sand dune","desert storm")
pokemon17=Pokemon("ninetales","fire","sinister","mind blast")
pokemon18=Pokemon("tyranitar","dark","drill blast","big bang attack")
pokemon19=Pokemon("infernape","fire","fire blast","fiery monk")
pokemon20=Pokemon("snorlax","normal","hungry shot","obesedian")
pokemon21=Pokemon("torterra","grass","grassy shot","earth pearce")
pokemon22=Pokemon("luxray","electric","accurate strike","lightning thunder")
pokemon23=Pokemon("scizor","steel","iron fist","ultra shield")
pokemon24=Pokemon("blastoise","water","water gun","water blast")
pokemon25=Pokemon("mudkip","water","radar","ultra radar")
pokemon26=Pokemon("garchomp","ground","meteor","sonic blast")
myPokemons=[pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6,pokemon7,pokemon8,pokemon9,pokemon10,pokemon11,pokemon12,pokemon13,pokemon14,pokemon15,pokemon16,pokemon17,pokemon18,pokemon19,pokemon20,pokemon21,pokemon22,pokemon23,pokemon24,pokemon25,pokemon26]
print("The Pokemons in the arsenal are: ")
time.sleep(0.5)
for i in range(len(myPokemons)):
    print(str(i+1)+": "+myPokemons[i].name.upper()+" of type "+myPokemons[i].pokeType.upper())
    time.sleep(0.5)
try:
    choice=int(input("Please choose your POKEMON by (entering the number before it): "))
except ValueError:
    print("Please enter a number")
selectedPokemon=""
print()
if(choice==1):
    selectedPokemon=myPokemons[0].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[0].health
    normalAtt=myPokemons[0].normalAttack
    speAtt=myPokemons[0].specialAttack
elif(choice==2):
    selectedPokemon=myPokemons[1].name.upper()
    print("you selected "+selectedPokemon)
    normalAtt=myPokemons[1].normalAttack
    speAtt=myPokemons[1].specialAttack
    health=myPokemons[1].health
elif(choice==3):
    selectedPokemon=myPokemons[2].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[2].health
    normalAtt=myPokemons[2].normalAttack
    speAtt=myPokemons[2].specialAttack
elif(choice==4): 
    selectedPokemon=myPokemons[3].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[3].health
    normalAtt=myPokemons[3].normalAttack
    speAtt=myPokemons[3].specialAttack
elif(choice==5):
    selectedPokemon=myPokemons[4].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[4].health
    normalAtt=myPokemons[4].normalAttack
    speAtt=myPokemons[4].specialAttack
elif(choice==6):
    selectedPokemon=myPokemons[5].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[5].health
    normalAtt=myPokemons[5].normalAttack
    speAtt=myPokemons[5].specialAttack
elif(choice==7):
    selectedPokemon=myPokemons[6].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[6].health
    normalAtt=myPokemons[6].normalAttack
    speAtt=myPokemons[6].specialAttack
elif(choice==8):
    selectedPokemon=myPokemons[7].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[7].health 
    normalAtt=myPokemons[7].normalAttack
    speAtt=myPokemons[7].specialAttack
elif(choice==9):
    selectedPokemon=myPokemons[8].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[8].health
    normalAtt=myPokemons[8].normalAttack
    speAtt=myPokemons[8].specialAttack
elif(choice==10):
    selectedPokemon=myPokemons[9].name.upper()
    print("you selected "+selectedPokemon) 
    health=myPokemons[9].health
    normalAtt=myPokemons[9].normalAttack
    speAtt=myPokemons[9].specialAttack
elif(choice==11):
    selectedPokemon=myPokemons[10].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[10].health
    normalAtt=myPokemons[10].normalAttack
    speAtt=myPokemons[10].specialAttack
elif(choice==12):
    selectedPokemon=myPokemons[11].name.upper()
    print("you selected "+selectedPokemon) 
    health=myPokemons[11].health 
    normalAtt=myPokemons[11].normalAttack
    speAtt=myPokemons[11].specialAttack
elif(choice==13):
    selectedPokemon=myPokemons[12].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[12].health
    normalAtt=myPokemons[12].normalAttack
    speAtt=myPokemons[12].specialAttack
elif(choice==14):
    selectedPokemon=myPokemons[13].name.upper()
    print("you selected "+selectedPokemon) 
    health=myPokemons[13].health
    normalAtt=myPokemons[13].normalAttack
    speAtt=myPokemons[13].specialAttack
elif(choice==15):
    selectedPokemon=myPokemons[14].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[14].health
    normalAtt=myPokemons[14].normalAttack
    speAtt=myPokemons[14].specialAttack
elif(choice==16):
    selectedPokemon=myPokemons[15].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[15].health
    normalAtt=myPokemons[15].normalAttack
    speAtt=myPokemons[15].specialAttack
elif(choice==17):
    selectedPokemon=myPokemons[16].name.upper()
    print("you selected "+selectedPokemon)
    normalAtt=myPokemons[16].normalAttack
    speAtt=myPokemons[16].specialAttack
    health=myPokemons[16].health
elif(choice==18):
    selectedPokemon=myPokemons[17].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[17].health
    normalAtt=myPokemons[17].normalAttack
    speAtt=myPokemons[17].specialAttack
elif(choice==19):
    selectedPokemon=myPokemons[18].name.upper()
    print("you selected "+selectedPokemon) 
    health=myPokemons[18].health
    normalAtt=myPokemons[18].normalAttack
    speAtt=myPokemons[18].specialAttack
elif(choice==20):
    selectedPokemon=myPokemons[19].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[19].health
    normalAtt=myPokemons[19].normalAttack
    speAtt=myPokemons[19].specialAttack
elif(choice==21):
    selectedPokemon=myPokemons[20].name.upper()
    print("you selected "+selectedPokemon) 
    health=myPokemons[20].health
    normalAtt=myPokemons[20].normalAttack
    speAtt=myPokemons[20].specialAttack
elif(choice==22):
    selectedPokemon=myPokemons[21].name.upper()
    print("you selected "+selectedPokemon) 
    health=myPokemons[21].health
    normalAtt=myPokemons[21].normalAttack
    speAtt=myPokemons[21].specialAttack
elif(choice==23):
    selectedPokemon=myPokemons[22].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[22].health
    normalAtt=myPokemons[22].normalAttack
    speAtt=myPokemons[22].specialAttack
elif(choice==24):
    selectedPokemon=myPokemons[23].name.upper()
    print("you selected "+selectedPokemon) 
    health=myPokemons[23].health
    normalAtt=myPokemons[23].normalAttack
    speAtt=myPokemons[23].specialAttack
elif(choice==25):
    selectedPokemon=myPokemons[24].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[24].health
    normalAtt=myPokemons[24].normalAttack
    speAtt=myPokemons[24].specialAttack
elif(choice==26):
    selectedPokemon=myPokemons[25].name.upper()
    print("you selected "+selectedPokemon)
    health=myPokemons[25].health
    normalAtt=myPokemons[25].normalAttack
    speAtt=myPokemons[25].specialAttack
else:
    print("please enter a valid POKEMON") 
rand=random.randint(1,25)
oponentPokemon=myPokemons[rand].name.upper()
opHealth=myPokemons[rand].health
opNormalAtt=myPokemons[rand].normalAttack
opSpeAtt=myPokemons[rand].specialAttack
time.sleep(1)
print("your opponent "+oponentPokemon)
print()
while(health>=0 and opHealth>=0):
    time.sleep(1)
    print("YOUR TURN")
    print("[1] "+normalAtt+" (normal attack)")
    print("[2] "+speAtt+" (special attack)")
    print("[3] recover health")
    yourMove=input("CHOOSE YOUR MOVE (by entering the number before the move)")
    print()
    if(yourMove=="1"):
        randAtt=random.randint(1,3)
        if(randAtt==1):
            print(selectedPokemon+" dealt 10 damage!")
            print()
            opHealth-=10
            time.sleep(1)
        elif(randAtt==2):
            print(oponentPokemon+" dodged your attack")
            print()
            time.sleep(1)
        else:
            print(oponentPokemon+" countered your attack")
            print()
            time.sleep(1)
            print(oponentPokemon+" dealt 15 damage")
            print()
            health-=15
            time.sleep(1)
    elif(yourMove=="2"):
        randAtt=random.randint(1,3)
        if(randAtt==1):
            print(selectedPokemon+" dealt 30 damage!")
            print()
            opHealth-=30
            time.sleep(1)
        elif(randAtt==2):
            print(oponentPokemon+" dodged your attack")
            print()
            time.sleep(1)
        else:
            print(oponentPokemon+" countered your attack")
            print()
            time.sleep(1)
            print(oponentPokemon+" dealt 40 damage!")
            print()
            health-=40
            time.sleep(1)
    else:
        print(selectedPokemon+" recovered 20 health")
        print()
        health+=20
        time.sleep(1)
    time.sleep(2)
    print("OPPONENT'S TURN")
    print()
    opRandAtt=random.randint(1,3)
    if(opRandAtt==1):
        opRandRandAtt=random.randint(1,3)
        if(opRandRandAtt==1):
            print(oponentPokemon+" dealt 10 damage!")
            print()
            health-=10
            time.sleep(1)
        elif(opRandRandAtt==2):
            print(selectedPokemon+" dodged the attack")
            print()
            time.sleep(1)
        else:
            print(selectedPokemon+" countered")
            print()
            time.sleep(1)
            print(selectedPokemon+" dealt 15 damage!")
            print()
            opHealth-=15
            time.sleep(1)
    elif(opRandAtt==2):
        opRandRandAtt=random.randint(1,3)
        if(opRandRandAtt==1):
            print(oponentPokemon+" dealt 30 damage!")
            print()
            health-=30
            time.sleep(1)
        elif(opRandRandAtt==2):
            print(selectedPokemon+" dodged the attack")
            print()
            time.sleep(1)
        else:
            print(selectedPokemon+" countered")
            print()
            time.sleep(1)
            print(oponentPokemon+" dealt 40 damage!")
            print()
            opHealth-=40
            time.sleep(1)
    else:
        print(oponentPokemon+" recovered 20 health")
        opHealth+=20
    time.sleep(2)
    print(selectedPokemon+"'S HEALTH: "+str(health))
    print()
    time.sleep(2)
    print(oponentPokemon+"'S HEALTH: "+str(opHealth))
    print()
if(health<=0):
    print("YOU LOST THE BATTLE")
    time.sleep(0.5)
    print()
    print(selectedPokemon+" LOST TO "+oponentPokemon)
else:
    print("YOU WON THE BATTLE")
    print()
    time.sleep(0.5)
    print(selectedPokemon+" DEFEATED "+oponentPokemon)
  
