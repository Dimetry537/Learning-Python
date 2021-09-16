class Item:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, o: str) -> bool:
        return self.name == o

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return self.name