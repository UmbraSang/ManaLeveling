from Characters.Hunter import Hunter


class NPC(Hunter):


    def __init__(self, name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages, hClass):
        super().__init__(name, stats, speeds, rank, hitDice, skills, damages, weapons, armours, languages, hClass)