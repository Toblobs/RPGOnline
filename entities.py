### RPGOnline
### A Synergy Studios Project

class Entity:

    """A class for every type of thing."""

    def __init__(self, id):

        self.id = id(self)


class Hero(Entity):

    """A hero which is represented a character which has a skillset
       and is controlled by a player."""


    def __init__(self):

        super().__init__(id)


h = Hero()
print(h.id)
        
