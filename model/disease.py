class Disease:
    def __init__(self, name: str, description: str, treatment: str):
        self.name = name
        self.description = description
        self.treatment = treatment

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def name(self, name: str):
        self._name = name
