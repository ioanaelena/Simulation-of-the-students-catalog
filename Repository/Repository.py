from typing import Protocol

from Domain.Entity import Entity


class Repository(Protocol):
    def read(self, idEntity=None):
        ...

    def adauga(self, entity: Entity):
        ...

    def sterge(self, idEntity: str):
        ...

    def modifica(self, idEntity:str, entity: Entity):
        ...