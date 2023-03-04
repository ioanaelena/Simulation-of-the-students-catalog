import jsonpickle

from Domain.Entity import Entity
from Repository.RepoInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writeFile(self) -> None:
        print(self.entitati)
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.entitati, indent=2))

    def loadFromFile(self) -> None:
        self.entitati = self.__readFile()

    def read(self, idEntitate=None):
        self.entitati = self.__readFile()
        return super().read(idEntitate)

    def adauga(self, entitate: Entity) -> None:
        self.entitati = self.__readFile()
        super().add(entitate)
        self.__writeFile()

    def sterge(self, idEntitate) -> None:
        self.entitati = self.__readFile()
        super().sterge(idEntitate)
        self.__writeFile()

    def modifica(self, idEntitate, entity:Entity) -> None:
        self.entitati = self.__readFile()
        super().modifica(entity.getIdEntity(), entity)
        self.__writeFile()