class Hogyegyek:
    def __init__(self, data):
        bomb = data.split(";")
        self.question1 = bomb[0]
        self.answerA = bomb[1]
        self.scoreA = int(bomb[2])
        self.answerB = bomb[3] 
        self.scoreB = int(bomb[4])
        self.answerC = bomb[5]
        self.scoreC = int(bomb[6])
        
