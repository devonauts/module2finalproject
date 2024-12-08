# Base Character class
import random
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        random_attack_damage = random.randrange(5,self.attack_power + 5)
        opponent.health -= random_attack_damage
        print(f"{self.name} attacks {opponent.name} for {random_attack_damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):
        if self.health < self.max_health :
             
             self.health += 20
             print(f'Health has been restored +20. Your current health level is {self.health}')
        else:  
            print(f'Your health is already at max level {self.health}')
            pass 

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    # Add your power attack method here

    def pillum_attack(self,opponent):
        damage = random.randrange(1, 30)
        total_damage = damage + self.attack_power
        opponent.health -= (total_damage)
        print(f"{self.name} has thrown a Roman Spear attack.It hit {opponent.name}'s health by {total_damage} ") 

    def double_sword_attack(self, opponent):
        damage = random.randrange(self.attack_power, self.attack_power + 20)
        opponent.health -= damage
        print(f"{self.name} has activated the double spin sword attack.It hit {opponent.name}'s health by {damage} ") 


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power
    
    def fireball(self, opponent):
        bonus_damage = random.randint(10, 20)
        total_damage = self.attack_power + bonus_damage
        opponent.health -= total_damage
        print(f"{self.name} casts Fireball! Deals {total_damage} damage to {opponent.name}.")

    def arcane_evasion(self):
        print(f"{self.name} uses Arcane Evasion to avoid the next attack!")
        self.evading = True


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=130,attack_power=15)
        self.evading = False
    
    def quick_shot(self, opponent ):
        print(f"{self.name} uses Quick Shot!")
        for _ in range(2):
            self.attack(opponent)
    
    def evade(self,opponent):
        print(f"{self.name} activates evade and will skip the next attack!")
        self.evading = True
        
    def reset_evade(self):
        self.evading = False
        print(f"{self.name}'s evade has worn off.")

class Palatin(Character):

    def __init__(self,name):
        super().__init__(name,health=130,attack_power=40)


    def holy_strike(self, opponent):
        bonus_damage = random.randint(10, 20)
        total_damage = self.attack_power + bonus_damage
        opponent.health -= total_damage
        print(f"{self.name} uses Holy Strike! Deals {total_damage} damage to {opponent.name}.")

    def divine_shield(self):
        print(f"{self.name} activates Divine Shield! They block the next attack.")
        self.evading = True

    def reset_evade(self):
        self.evading = False
        print(f"{self.name}'s Divine Shield has worn off.")

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

    def dark_blast(self, opponent):
        multiplier = random.uniform(1.5, 2.0)
        damage = int(self.attack_power * multiplier)
        opponent.health -= damage
        print(f"{self.name} uses Dark Blast! Deals {damage} damage to {opponent.name}.")

    def take_turn(self, opponent):
        if getattr(opponent,"evading", False):
            print(f"{opponent.name} evaded the attack from {self.name}!")
            opponent.reset_evade()
        else:
            action = random.choice(["attack", "dark_blast"])
            if action == "attack":
                self.attack(opponent)
            elif action == "dark_blast":
                self.dark_blast(opponent)

# Function to create player character based on user input
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")  # Add Archer
    print("4. Paladin")  # Add Paladin
    
    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Palatin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

# Battle function with user menu for actions
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
        elif choice == '2':
            if isinstance(player,Warrior):
                sub_choice = input("Choose: 1. Pillum Attack, 2. Double Sword Attack: ")
                if sub_choice == '1':
                    player.pillum_attack(wizard)
                elif sub_choice == '2':
                    player.double_sword_attack(wizard)
            if isinstance(player, Mage):
                sub_choice = input("Choose: 1. Fireball, 2. Arcane Evasion: ")
                if sub_choice == '1':
                    player.fireball(wizard)
                elif sub_choice == '2':
                    player.arcane_evasion()
            elif isinstance(player, Archer):
                sub_choice = input("Choose: 1. Quick Shot, 2. Evade: ")
                if sub_choice == '1':
                    player.quick_shot(wizard)
                elif sub_choice == '2':
                    player.evade(wizard)
            elif isinstance(player, Palatin):
                sub_choice = input("Choose: 1. Holy Strike, 2. Divine Shield: ")
                if sub_choice == '1':
                    player.holy_strike(wizard)
                elif sub_choice == '2':
                    player.divine_shield()
        elif choice == '3':
            player.heal()
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard.regenerate()
            wizard.take_turn(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

        if wizard.health <= 0:
            print(f"The wizard {wizard.name} has been defeated by {player.name}!")


# Main function to handle the flow of the game
def main():
    # Character creation phase
    player = create_character()

    # Evil Wizard is created
    wizard = EvilWizard("The Dark Wizard")

    # Start the battle
    battle(player, wizard)

if __name__ == "__main__":
    main()