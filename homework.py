# Example 1
# buddy = Animal('Buddy', 10)
# buddy.play(5) -> "Buddy is playing for 5 minutes. His energy is now 5"
# buddy.sleep(10) -> "Buddy is sleeping for 5 minutes. His energy is now 15"
# TODO vvvvvvvvvvvvv The calculation is incorrect because when it's making the sleeping calculation, it's adding the sum to the original energy level and printing instead of
# inheriting the new energy level from def playing
class PascalMonster():
    energy_level = 100
    pass
    def __init__(self, name, attribute):
        self.name = name
        self.attribute = attribute
    
    def playing(self, play_action):
        new_energy_level = self.energy_level - (play_action//4)
        print(f'After playing for a few minutes, {pascalmonster1.name}\'s energy level is now: {new_energy_level}')
        

    def sleeping(self, sleeping_action):
        new_energy_level = self.energy_level + (2 * sleeping_action)
        print(f'After sleeping for a while, {pascalmonster1.name}\'s energy level is now: {new_energy_level}')
        

pascalmonster1 = PascalMonster('Floeamon', 'Ice/Water')
pascalmonster1.energy_level = 100
print(f'{pascalmonster1.name} is an {pascalmonster1.attribute} type PascalMonster.')
print(f'{pascalmonster1.name}\'s energy level is currently: {pascalmonster1.energy_level}')
pascalmonster1.playing(100)
pascalmonster1.sleeping(10)