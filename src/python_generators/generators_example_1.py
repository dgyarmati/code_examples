class StarDestroyer():
    blast = "POW!"

    def fire_plasma_cannon(self):
        return self.blast

star_destroyer = StarDestroyer()
print(star_destroyer.fire_plasma_cannon(), end=" ")