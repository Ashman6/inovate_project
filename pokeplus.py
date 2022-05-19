from shutil import move
import time
import numpy as np
import sys

# delay printing

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)




class pokemon:
    def __init__(self, name, types, moves, EVs, health='==============='):

        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defence = EVs['DEFENCE']
        self.health = health
        self.bars = 20 #health


        def fight(self, pokemon2):
            print("-----POKEMON BATTLE-----")
            print(f"\n{self.name}")
            print("TYPE/", self.types)
            print("ATTACK/", self.attack)
            print("DEFENCE/", self.defence)
            print("LVL/", 3*(1+np.mean([self.attack,self.defence])))
            print("\nVS")
            print(f"\n{pokemon2.name}")
            print("TYPE/", pokemon2.types)
            print("ATTACK/", pokemon2.attack)
            print("DEFENCE/", pokemon2.defence)
            print("LVL/", 3*(1+np.mean([pokemon2.attack,pokemon2.defence])))


            time.sleep(2)

            version = ['fire', 'water', 'grass']
            for i,k in enumerate(version):
                if self.types == k:
                    if pokemon2.types == k:
                        string_1_attack ='its not very effective...'
                        string_2_attack ='its not very effective...'


                    if pokemon2.types == version[(i+1)%3]:
                        pokemon2.attack *= 2  
                        pokemon2.defence *= 2 
                        self.attack /= 2
                        self.defence /= 2
                        string_1_attack ='its not very effective...'
                        string_2_attack ='its super effective!...'


                    if pokemon2.types == version[(i+2)%3]:
                        pokemon2.attack *= 2  
                        pokemon2.defence *= 2 
                        self.attack /= 2
                        self.defence /= 2
                        string_1_attack ='its super effective!...'
                        string_2_attack ='its not very effective...'


            while (self.bars > 0) and (pokemon2.bars > 0):
                print (f"{self.name}\t\tHLTH\t{self.health}")
                print (f"{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n")
                
                print(f"go {self.name}!")

                for i, x in enumerate(self.moves):
                    print(f"{i+1}.", x)
                    
                index = int(input('pick a move: '))
                delay_print(f"{self.name} used {self.moves[index-1]}!")

                time.sleep(1)
                delay_print(string_1_attack)

                pokemon2.bars -= self.attack
                pokemon2.health = ""  

                for j in range(int(pokemon2.bars+.1*pokemon2.defence)):
                    pokemon2.health += "="

                time.sleep(1)
                print (f"{self.name}\t\tHLTH\t{self.health}")
                print (f"{pokemon2.name}\t\tHLTH\t{pokemon2.health}\n")
                time.sleep(.5)

                if pokemon2.bar<= 0:
                    delay_print("\n..." + 'fainted')
                    break


                print(f"go {self.name}!")

                for i, x in enumerate(pokemon2.moves):
                    print(f"{i+1}.", x)
                    
                index = int(input('pick a move: '))
                delay_print(f"{pokemon2.name} used {pokemon2.moves[index-1]}!")

                time.sleep(1)
                delay_print(string_2_attack)

                self.bars -= pokemon2.attack
                self.health = ""  

                for j in range(int(self.bars+.1*self.defence)):
                    self.health += "="

                time.sleep(1)
                print (f"{pokemon2.name}\t\tHLTH\t{pokemon2.health}")
                print (f"{self.name}\t\tHLTH\t{self.health}\n")
                time.sleep(.5)

                if self.bar<= 0:
                    delay_print("\n..." + self.name + 'fainted')
                    break

        money = np.random.choice(5000)
        delay_print(f"opponent paid you £{money}.")




if __name__ == '__main__':
    pass





