class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if self.id is not None:
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
        