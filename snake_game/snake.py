class  Snake:
    
    def  __init__(self, player) -> None:
        self.fragments = [[20, 20], [20, 21], [20, 22], [20, 23]]
        self.head = self.fragments[0]
        self.speed = 20
        self.player = player
        