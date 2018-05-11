from random import *

def Main():
    
    #generic pokemon class
    class Pokemon():
        pType=""
        player=0
        name=""
        moveSet=[]
        health=0
        attack=0
        defense=0
        status=0
        accuracy=6
        def statsDescription(self):
            stats= "HP: %s, ATK: %s, DEF: %s" %(self.health, self.attack, self.defense)
            return stats
            
    #move creation class
    class move():
        def __init__(self, mType, name, status, damage, PPRemaining):
            self.mType=mType
            self.name=name
            self.status=status
            self.damage=damage
            self.PPRemaining=PPRemaining
    class pokeMove(move):
        def __init__(self, mType, name, status, damage, PPRemaining, pokeUse, accuracy):
            move.__init__(self, mType, name, status, damage, PPRemaining)
            self.pokeUse=pokeUse
            self.accuracy=accuracy
            
    #Pokemon take damage method        
    def takeDamage(recipient, move, attacker):
        move.PPRemaining-=1
        print('%s has %s PP remaining' %(move.name, move.PPRemaining))
        hit=(randint(0,100)+attacker.accuracy)/2
        if hit<=move.accuracy:
            print("%s has hit" %(move.name))
            if move.status!="no":
                if move.status=="ATKDown":
                    recipient.status.append(["ATKDown", 3])
                    recipient.attack-=5
                    print("%s attack has been lowered" %(recipient.name))
                elif move.status=="leechSeed":
                    recipient.status.append(["leechSeed", 3])
                    print("A leech seed has been planted on %s" %(recipient.name))
                elif move.status=="burn":
                    recipient.status.append(["burn", 3])
                    print("%s has been burned" %(recipient.name))
                elif move.status=="DEFUp":
                    attacker.status.append(["DEFUp", 3])
                    attacker.defense+=5
                elif move.status=="ACCDown":
                    recipient.status.append(["ACCDown", 3])
                    recipient.accuracy-=10
                elif move.status=="DEFDown":
                    recipient.status.append(["DEFDown"])
                    recipient.defense-=10
            if move.damage!=0:
                dmgRange=randint(-5, 5)
                amount=(attacker.attack)+dmgRange-recipient.defense+move.damage
                damage=type_effect(move.mType, recipient.pType, amount)
                recipient.health-=damage
                damageStatement="%s has taken %s damage, and now has %s health" %(recipient.name, damage, recipient.health)
                print(damageStatement)
            else:
                print("%s has missed" %(move.name))
    
    #status effect
    def takeStatus(recipient, attacker):
        for [i, j] in recipient.status:
            if j>0:
                if "leechSeed" in recipient.status:
                    recipient.health-=5
                    attacker.health+=5
                    print("%s has taken 5 damage and now has %s health. %s has healed 5 health and now has %s health." %(recipient.name, recipient.health, attacker.name, attacker.health))
                if "burn" in recipient.status:
                    recipient.health-=5
                    print("%s has been burned for 5 damage and now has %s health." %(recipient.name, recipient.health))
            if j==0:
                if "ATKDown" in recipient.status:
                    recipient.attack+=5
                    recipient.status=[x for x in recipient.status if x[1]!=0]
                    print('%s attack has returned to normal' %(recipient.name))
                elif "leechSeed" in recipient.status:
                    recipient.status=[x for x in recipient.status if x[1]!=0]
                    print('The leech seed in %s has stopped working' %(recipient.name))
                elif "DEFDown" in recipient.status:
                    recipient.defense+=10
                    recipient.status=[x for x in recipient.status if x[1]!=0]
                    print('%s defense has returned to normal' %(recipient.name))
                elif "ACCDown" in recipient.status:
                    recipient.accuracy+=10
                    recipient.status=[x for x in recipient.status if x[1]!=0]
                    print('%s accuracy has returned to normal' %(recipient.name))
                elif "burn" in recipient.status:
                    recipient.status=[x for x in recipient.status if x[1]!=0]
                    print('%s is no longer on fire' %(recipient.name))
            if attacker.status==0:
                if "DEFUp" in attacker.status:
                    attacker.defense-=5
                    recipient.status=[x for x in attacker.status if x[1]!=0]
                    print('%s defense has recurned to normal' %(attacker.name))

    #Turn based combat method
    def turn(p1Poke, p2Poke, turn):
        p1Poke=a_pokemon[p1Poke]
        p2Poke=a_pokemon[p2Poke]
        t=turn
        while p1Poke.health>0 and p2Poke.health>0:
            if t==1:
                t=2
            elif t==2:
                t=1
            if t==1:
                print('Player 1s turn')
                print(p1Poke.name)
                takeStatus(p1Poke, p2Poke)
                for [i, j] in p1Poke.status:
                    if j>0 in p1Poke.status:
                        p1Poke.status=[[i, j-1] for i, j in p1Poke.status]
                def p1Turn():
                    print(p1Poke.moveSet)
                    move=""
                    while move not in p1Poke.moveSet:
                        move=str(input('select a move\n'))
                    if p1Poke==a_pokemon["Bulbasaur"]:
                        move=move+'B'
                    elif p1Poke==a_pokemon["Charmander"]:
                        move=move+'C'
                    elif p1Poke==a_pokemon["Squirtle"]:
                        move=move+'S'
                    if a_move[move].PPRemaining==0:
                        print('%s is out of PP, choose a different move' %(a_move[move].name))
                        p1Turn()
                    takeDamage(p2Poke, a_move[move], p1Poke)
                p1Turn()
            if t==2:
                print('Player 2s turn')
                print(p2Poke.name)
                takeStatus(p2Poke, p1Poke)
                for [i, j] in p2Poke.status:
                    if j>0 in p2Poke.status:
                        p2Poke.status=[[i, j-1] for i, j in p2Poke.status]
                def p2Turn():
                    print(p2Poke.moveSet)
                    move=""
                    while move not in p2Poke.moveSet:
                        move=input('select a move\n')
                    if p2Poke==a_pokemon["Bulbasaur"]:
                        move=move+'B'
                    elif p2Poke==a_pokemon["Charmander"]:
                        move=move+'C'
                    elif p2Poke==a_pokemon["Squirtle"]:
                        move=move+'S'
                    if a_move[move].PPRemaining==0:
                        print('%s is out of PP, choose a different move' %(a_move[move].name))
                        p2Turn()
                    takeDamage(p1Poke, a_move[move], p2Poke)
                p2Turn()
        if p1Poke.health>0:
            print('Player 1 has won!')
        elif p2Poke.health>0:
            print('Player 2 has won!')
                
    #type effectiveness
    def type_effect(moveType, pokeType, damage):
        effective=1
        if moveType=="grass":
            if pokeType=="water":
                effective=2
                damage*=2.0
            elif pokeType=="grass":
                damage*=.5
                effective=0
        elif moveType=="fire":
            if pokeType=="grass":
                damage*=2.0
                effective=2
            elif pokeType=="water":
                damage*=.5
                effective=0
        elif moveType=="water":
            if pokeType=="fire":
                damage*=2.0
                effective=2
            elif pokeType=="grass":
                damage*=.5
                effective=0
        if effective==0:
            print('It was not very effective')
        elif effective==2:
            print('It was super effective!')
        return damage
            
        
    #initialization
    a_pokemon={}
    a_move={}
    def initializePokemon(pokemon, player):
        #setup for bulbasaur
        if pokemon=="Bulbasaur":
            Bulbasaur=Pokemon()
            Bulbasaur.pType="grass"
            Bulbasaur.name="Bulbasaur"
            Bulbasaur.health=45
            Bulbasaur.attack=49
            Bulbasaur.defense=49
            Bulbasaur.status=[]
            Bulbasaur.player=player
            
            tackleB=pokeMove("normal", "tackle", "no", 10, 15, Bulbasaur, 90)
            a_move["tackleB"]=tackleB
            growlB=pokeMove("normal", "growl", "ATKDown", 0, 15, Bulbasaur, 100)
            a_move["growlB"]=growlB
            vineWhipB=pokeMove("grass", "vineWhip", "no", 13, 10, Bulbasaur, 85)
            a_move["vineWhipB"]=vineWhipB
            leechSeedB=pokeMove("grass", "leechSeed", "leechSeed", 0, 5, Bulbasaur, 80)
            a_move["leechSeedB"]=leechSeedB
            
            Bulbasaur.moveSet=[tackleB.name, growlB.name, vineWhipB.name, leechSeedB.name]
            a_pokemon["Bulbasaur"]=Bulbasaur
            
        #setup for charmander
        elif pokemon=="Charmander":
            Charmander=Pokemon()
            Charmander.pType="fire"
            Charmander.name="Charmander"
            Charmander.health=39
            Charmander.attack=52
            Charmander.defense=52
            Charmander.status=[]
            
            scratchC=pokeMove("normal", "scratch", "no", 12, 15, Charmander, 90)
            a_move["scratchC"]=scratchC
            growlC=pokeMove("normal", "growl", "ATKDown", 0, 15, Charmander, 100)
            a_move["growlC"]=growlC
            emberC=pokeMove("fire", "ember", "burn", 10, 15, Charmander, 85)
            a_move["emberC"]=emberC
            smokeScreenC=pokeMove("fire", "smokeScreen", "ACCDown", 0, 15, Charmander, 90)
            a_move["smokeScreenC"]=smokeScreenC
            
            Charmander.moveSet=[growlC.name, scratchC.name, emberC.name, smokeScreenC.name]
            a_pokemon["Charmander"]=Charmander
            
        #setup for squirtle
        elif pokemon=="Squirtle":
            Squirtle=Pokemon()
            Squirtle.pType="water"
            Squirtle.name="Squirtle"
            Squirtle.health=44
            Squirtle.attack=48
            Squirtle.defense=65
            Squirtle.status=0
            Squirtle.status=[]
            
            tackleS=pokeMove("normal", "tackle", "no", 10, 15, Squirtle, 90)
            a_move["tackleS"]=tackleS
            tailWhipS=pokeMove("normal", "tailWhip", "DEFDown", 0, 15, Squirtle, 100)
            a_move["tailWhipS"]=tailWhipS
            waterGunS=pokeMove("water", "waterGun", "no", 13, 10, Squirtle, 85)
            a_move["waterGunS"]=waterGunS
            withdrawS=pokeMove("normal", "withdraw", "DEFUp", 0, 15, Squirtle, 90)
            a_move["withdrawS"]=withdrawS
            
            Squirtle.moveset=[tackleS.name, tailWhipS.name, waterGunS.name, withdrawS.name]
            a_pokemon["Squirtle"]=Squirtle
            
    #game start algorithm, choose pokemon
    p1Poke=0
    while p1Poke!="Bulbasaur" and p1Poke!="Charmander" and p1Poke!="Squirtle":
        p1Poke=str(input('Player 1, which pokemon do you want, Bulbasaur, Charmander, or Squirtle?\n'))
    initializePokemon(p1Poke, 1)
    p2Poke=0
    while p2Poke!="Bulbasaur" and p2Poke!="Charmander" and p2Poke!="Squirtle":
        p2Poke=str(input('Player 2, which pokemon do you want, Bulbasaur, Charmander, or Squirtle?\n'))
    initializePokemon(p2Poke, 2)
    turn(p1Poke, p2Poke, 2)

Main()