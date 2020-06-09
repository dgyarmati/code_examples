class StarDestroyer():
    blast = "POW!"

    def fire_plasma_cannon(self):
        yield self.blast

star_destroyer = StarDestroyer()

print(next(star_destroyer.fire_plasma_cannon()), end=" ")