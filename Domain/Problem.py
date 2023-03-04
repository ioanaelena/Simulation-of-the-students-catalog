from Domain.Entity import Entity

class Problema(Entity):
    def __init__(self, idEntity, description, deadline):
        super().__init__(idEntity)
        self.__description = description
        self.__deadline = deadline

    def getDescription(self):
        return self.__description

    def getDeadline(self):
        return self.__deadline

    def setDescription(self, description):
        self.__description = description

    def setDeadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return f"Nr__lab_Nr__Problem: {self.getIdEntity()}, description: {self.__description}, deadline: {self.__deadline}"