import random

class  Apple:
    
    def __init__(self) -> None:
        self.apple = [10, 5]
        
    def regenerate(self):
        self.x = random.randint(1, 40)
        self.y = random.randint(1, 40)
        
apple = Apple()
apple.regenerate()
print(f"{apple.x}, {apple.y}")
        