import json
from dataclasses import dataclass, field

class PersonBuilder:
    def __init__(self):
        self._person = None
    
    def person(self):
        self._person = Person()
        return self

    def name(self, name: str):
        self._person.name = name
        return self

    def surname(self, surname: str):
        self._person.surname = surname
        return self
    
    def person_id(self, person_id: int):
        self._person.person_id = person_id
        return self
    
    def build(self):
        return self._person

@dataclass(frozen=False, order=True)
class Person:
    person_id: int = field(default=0)
    name: str = field(default="")
    surname: str = field(default="")

    def to_json(self) -> str:
        return json.dumps(self.__dict__)