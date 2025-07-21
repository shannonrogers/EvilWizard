# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")
        
    
    
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=25)
        self.spattack = 2
        self.potion = 1
        
    def special_attack(self,opponent):
            special_damage = 45
            if self.spattack > 0:
                opponent.health -= special_damage
                print(f"{self.name} used a poison arrow for 45 damage!")
                self.spattack -= 1
                if opponent.health <= 0:
                    print(f"{opponent.name} has been defeated!")
            else:
                print(f"{self.name} is out of poison arrows, choose again")


    
    def heal(self):
        if self.health < self.max_health - 30 and self.potion > 0:
            self.health += 30
            print(f"{self.name} took a healing potion and regerated 30 health! Current health: {self.health}")
            self.potion -= 1
        elif self.potion == 0:
            print(f"{self.name} does not have any more healing potions")
        else:
            print(f"{self.name} has not taken enough damage to heal")
        
  
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)
        self.potion = 1
        self.spattack = 2
    
    def heal(self):
        if self.health < self.max_health and self.potion > 0:
            self.health += 45
            print(f"{self.name} is surrounded in a warm light and heals for 45 health! Current health: {self.health}")
            self.potion -= 1
        elif self.potion == 0:
            print(f"{self.name} the heavens are occupied elsewhere")
        else:
            print(f"{self.name} has not taken enough damage to heal")

    def special_attack(self, opponent):
        special_damage = 35
        if self.spattack > 0:
            opponent.health -= special_damage
            print(f"A bright flash of light boosts {self.name}'s attack for 35 points of damage")
            self.spattack -=1
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print(f"It seems nothing is coming to your aid, you will need to fight the remainder of this battle on your own")

        

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=45)
        self.potion = 1
        self.spattack = 2
    
    def heal(self):
        if self.health < self.max_health - 30 and self.potion > 0:
            self.health += 30
            print(f"{self.name} took a healing potion and regerated 15 health! Current health: {self.health}")
            self.potion -= 1
        elif self.potion == 0:
            print(f"{self.name} does not have any more healing potions")
        else:
            print(f"{self.name} has not taken enough damage to heal")

    def special_attack(self,opponent):
        special_damage = 35
        if self.spattack > 0:
            opponent.health -= special_damage
            print(f"{self.name} used whirlwind axe for 35 damage!")
            self.spattack -= 1
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print(f"your axes break, use your sword")

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=35)
        self.potion = 1
        self.spattack = 2

    def heal(self):
        if self.health < self.max_health - 30 and self.potion > 0:
            self.health += 30
            print(f"{self.name} took a healing potion and regerated 30 health! Current health: {self.health}")
            self.potion -= 1
        elif self.potion == 0:
            print(f"{self.name} does not have any more healing potions")
        else:
            print(f"{self.name} has not taken enough damage to heal")

    def special_attack(self,opponent):
        special_damage = 45
        if self.spattack > 0:
            opponent.health -= special_damage
            print(f"{self.name} created a storm of fire dealing 45 damage!")
            self.spattack -= 1
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            print(f"It starts raining, the fire won't answer your call")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")



def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer") #Potential Class Add on
    print("4. Paladin")  #Potential Class Add on

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
            if wizard.health > 0:
                wizard.regenerate()
                wizard.attack(player)
        elif choice == '2':
            player.special_attack(wizard)
            if wizard.health > 0:
                wizard.regenerate()
                wizard.attack(player)
        elif choice == '3':
            player.heal()
            if wizard.health > 0:
                wizard.regenerate()
                wizard.attack(player)
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break
           
    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

# if __name__ == "__main__":
main()