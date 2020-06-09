import random


class StarDestroyer():
    def fire_plasma_cannon(self):
        plasma_blast_generator = self.generate_plasma_blast()
        plasma_blast_generator.send(None)

        while True:
            blast_sound = self.get_random_plasma_blast_sound()
            print(plasma_blast_generator.send(blast_sound), end=" ")

    def get_random_plasma_blast_sound(self):
        blast_sounds = ["POW!", "BLAM!", "ZIIING!", "ZZZAAPP!", "KA-BLAM!"]
        return random.choice(blast_sounds)

    def generate_plasma_blast(self, blast_sound="POW!"):
        while True:
            blast_sound = yield blast_sound


StarDestroyer().fire_plasma_cannon()