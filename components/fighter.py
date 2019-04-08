import tcod as libtcod

from game_messages import Message

class Fighter:
    def __init__(self, hp, defense, power, mp=0, exp=0):
        self.max_hp     = hp
        self.hp         = hp
        self.defense    = defense
        self.power      = power
        self.max_mp     = mp
        self.mp         = mp
        self.exp        = exp

    def take_damage(self, amount):
        results = []
        self.hp -= amount

        if self.hp <= 0:
            results.append({ 'dead': self.owner, 'exp': self.exp })

        return results

    def heal(self, amount, ignore_max=False):
        self.hp += amount

        if ignore_max or self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack(self, target):
        results = []
        damage  = self.power - target.fighter.defense

        if damage > 0:
            results.append({'message': Message('{0} attacks {1} for {2} hit points.'.format(
                self.owner.name.capitalize(), target.name, str(damage)), libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({'message': Message('{0} attacks {1} but does no damage.'.format(
                self.owner.name.capitalize(), target.name), libtcod.white)})
        return results
