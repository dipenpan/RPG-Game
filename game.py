import random
from playsound import playsound 

# Define a function to play sounds
sounds = {
    'attack': 'attack_sound.mp3',  # Just the filename if in the same directory
    'potion': 'potion_sound.mp3',
    'win': 'win_sound.mp3',
    'lose': 'lose_sound.mp3'
}

# Art for visualization
def print_creature(creature_name):
    art = {
       'monster': "👹",
       'rabbit' : "🐇",
       'fox' : "🦊",
       'rat': "🐀",
    }
    print(art.get(creature_name, "❓"))

# Game constants and variables
PLAYER_HEALTH = 20
PLAYER_COINS = 0
PLAYER_INVENTORY = []
PLAYER_ARMOR = 0

CREATURES = {
    'monster': {"health": 10, "attack": 5, "drop": "potion"},
    'rabbit': {'health': 3, 'attack': 1, "drop": None},
    'fox': {'health': 5, 'attack': 3, "drop": None},
    'rat': {'health': 2, 'attack': 2, "drop": None}
}

ITEMS = ['helmet', 'shield', 'boots', 'chest plate', 'gauntlets']
OTHER_THINGS = ['bush', 'big tree', 'rock']

ALL_THINGS = list(CREATURES.keys()) + ITEMS + OTHER_THINGS

# MAIN GAME LOOP
while PLAYER_HEALTH > 0 and PLAYER_COINS < 100:
    print("\033[H\033[2J", end="")  # Clear screen
    print(f"HEALTH = {PLAYER_HEALTH} Items: {','.join(PLAYER_INVENTORY)} Coins: {PLAYER_COINS}\n")
    
    # Random encounter
    current_thing = random.choice(ALL_THINGS)
    print(f"You encounter a {current_thing}!")
    print_creature(current_thing)  # Print creature art

    # If it's an item
    if current_thing in ITEMS and current_thing not in PLAYER_INVENTORY:
        print(f"You found a {current_thing}!")
        PLAYER_INVENTORY.append(current_thing)
        PLAYER_ARMOR += 1
        print(f"Your armor has increased! Armor: {PLAYER_ARMOR}")
        
    # If it's a creature
    elif current_thing in CREATURES:
        creature = CREATURES[current_thing]
        health = creature['health']
        print(f"A wild {current_thing} appears with {health} health!")
        
        response = input("Do you want to fight or run? (fight/run): ").lower()
        if response == 'run':
            print("You manage to escape!")
            continue

        # Fight sequence
        while health > 0 and PLAYER_HEALTH > 0:
            attack_amount = random.randint(1, 5) + PLAYER_ARMOR
            health -= attack_amount
            print(f"You attack the {current_thing} for {attack_amount} damage!")
            playsound(sounds['attack'])

            if health <= 0:
                print(f"You defeated the {current_thing}!")
                PLAYER_COINS += 10
                if creature["drop"] == "potion" and random.random() < 0.5:
                    print("The monster dropped a healing potion!")
                    playsound(sounds['potion'])
                    PLAYER_HEALTH += 5
                    print("You used the potion and gained 5 health.")

            # Creature's counter-attack
            creature_attack = random.randint(1, creature['attack'])
            PLAYER_HEALTH -= creature_attack
            print(f"The {current_thing} attacks you for {creature_attack} damage!")
            print(f"Your health is now {PLAYER_HEALTH}")

            if PLAYER_HEALTH <= 0:
                print("GAME OVER! You have been defeated! 😔")
                playsound(sounds['lose'])
                break
        
        # Win condition check
        if PLAYER_COINS >= 100:
            print("CONGRATULATIONS! 😊 You earned 100 coins and won the game!")
            playsound(sounds['win'])
            break  # Exit the loop once the player wins

    # Wait to continue the journey
    input("Press ENTER to continue your journey...")

# End game message
print("Thank you for playing!")

