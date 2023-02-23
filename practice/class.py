class Cars:
    def __init__(self, color = '', seat = 0):
        self.color = color
        self.seat = seat
    
    def drive(self):
        print(f"My car is {self.color} and has {self.seat} seats.")
    def Way(self):
        print("NO")

mazda = Cars("blue", 4)
mazda.drive()
mazda.Way()
print(mazda)




