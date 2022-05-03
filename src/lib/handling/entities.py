### RPGOnline
### A Synergy Studios Project

import random

# - GAME CLASSES - #

class Game:

    """A class for a single game that stores all the other classes.
       For now, this refers to local-game only classes."""

    def __init__(self):

        self.players = {} #PlayerID, PlayerClass

class Shop:

    """A class to represent the shop, in which players can buy from."""

    pass

# - ENTITY CLASSES - #

class Entity:

    """A class for every type of thing.

       Health: Health Left
       Moveset: Moves/Attacks to be used on other entites
       Seletced Attack: The selected Move/Attack you have
       Defence: Scale from 1 - 100, percentage of damage negated
       Agility: Speed of entity
       Effects Applied: Any effects on this entity

    """

    def __init__(self, gametag, name, health, moveset, defence, agility):

        self.gametag = gametag
        self.name = name

        self.health = health
        self.moveset = moveset
        self.selected_attack = None
        self.defence = defence
        self.agility = agility

        self.effects_applied = []

        self.stats = [self.health, self.moveset, self.selected_attack, self.defence, self.agility, self.effects_applied]

    def refresh_stats(self):

        """Refreshes the statistics (for save/load purposes)"""

        self.stats = [self.health, self.moveset, self.selected_attack, self.defence, self.agility, self.effects_applied]

    def defend_attack(self, entity_from, damage):

        """Defends an attack from another entity."""

        print(f'Entity {entity_from.name} attacked!')

        defence = (self.defence / 100)
        total_damage = damage - (damage * defence)

        self.health = (self.health - total_damage)

        print(f'Lost {total_damage} hp!')

class Hero(Entity):

    """A hero which is represented a character which has a skillset
       and is controlled by a player."""

    def __init__(self, gametag, name, health, moveset, defence, agility, level)

        super().__init__(gametag, name, health, moveset, selected_attack, defence, agility, effects_applied)
        
        self.level = level

    def refresh_stats(self):

        """Refreshes the statistics (for save/load purposes)"""

        self.stats = [self.health, self.moveset, self.selected_attack, self.defence, self.agility, self.effects_applied, self.level]
        
class Monster(Entity):

    """A monster which attacks heroes and has different moves."""

    pass


class NPC(Entity):

    """NPCs in which the players can interact with."""

    def __init__(self, gametag, name, speech, stats):

        super().__init__(gametag, name)
        self.speech = speech

        self.stats = [self.gametag, self.name, self.speech, self.stats]

    def refresh_stats(self):

        """Refreshes the statistics (for save/load purposes)"""

        self.stats = [self.gametag, self.name, self.speech, self.stats]

    def play_speech(self):

        """Plays the speech of the NPC."""

        pass

# - MOVESET CLASSES - #

class Move:

    """A move that an entity uses in a battle to affect other players."""

    def __init__(self, name):
        
        self.name = name


class Attack(Move):

    """A move which damages another entity.

       Name: The name of the attack
       Damage: Base damage points (HP)
       Crit Chance: 1/x chance that you get a boost
       Crit Boost: Damage boost applied when you get a crit
       Miss Chance: 1/x chance you miss

    """

    def __init__(self, name, damage, crit_chance, crit_buff, miss_chance):

        super().__init__(name)

        self.damage = damage
        
        self.crit_chance = crit_chance
        self.crit_buff = crit_buff

        self.miss_chance = miss_chance


    def attack_entity(self, en, entity_from):

        """Attacks a particular entity."""

        miss = random.randint(1, self.miss_chance)

        if miss < (self.miss_chance - 1): # If miss_chance = 5, chance = 1/5

            crit = random.randint(1, self.crit_chance)

            if crit > (self.crit_chance - 1): # If crit_chance = 5, chance = 1/5
                total_damage = self.damage + self.crit_buff
                print('Critical Hit!')

            else:
                total_damage = self.damage
                print('Hit!')

            en.defend_attack(entity_from, total_damage) # This entity defends it

        else:
            print('Missed Attack!')

class Spell(Move):

    """A move that applies an effect to an entity."""

    def __init__(self, name):

        super().__init__(name)




# - EFFECT CLASSES - #

class Effect:

    """An effect which is applied onto an entity.

       Name: Name of effect
       
    """

    def __init__(self, name):

        self.name = name
    
