class StarDestroyer():
    blast = "POW!"

    def fire_plasma_cannon(self):
        while True:
            yield self.blast

star_destroyer = StarDestroyer()

for blast in star_destroyer.fire_plasma_cannon():
    print(blast, end=" ")