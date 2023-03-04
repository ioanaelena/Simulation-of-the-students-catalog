from Domain.Entity import Entity
class Student(Entity):
    def __init__(self,idEntity,nume,nrPrezente,nota):
        super().__init__(idEntity)
        self.__nume = nume
        self.__nrPrezente = nrPrezente
        self.__nota = nota

    def getNume(self):
        return self.__nume

    def getNrPrezente(self):
        return self.__nrPrezente

    def getNota(self):
        return self.__nota

    def setNume(self, nume):
        self.__nume = nume

    def setNrPrezente(self,nrPrezente):
        self.__nrPrezente = nrPrezente

    def setNota(self,nota):
        self.__nota = nota

    def __str__(self):
        return f"id: {self.getIdEntity()}, nume: {self.__nume}, nrPrezente: {self.__nrPrezente}, nota:{self.__nota}"