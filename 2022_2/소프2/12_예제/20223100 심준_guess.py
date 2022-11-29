class Guess:
    secretWord = ""
    numTries = 0
    guessedChars = []
    currentStatus = ""
    def __init__(self, word):
        self.secretWord = word
        for i in range(len(word)):
            self.currentStatus+="_"

    def display(self):
        print("Current: "+ self.currentStatus)
        print("Tries: " + str(self.numTries))


    def guess(self, character):
        self.guessedChars.append(character)
        if character in self.secretWord:
            for i in range(len(self.secretWord)):
                if(self.secretWord[i] == character):
                    L = list(self.currentStatus)
                    L[i]= character
                    self.currentStatus = "".join(L)
        else:
            self.numTries+=1
        if self.secretWord == self.currentStatus:
            return True
        else:
            return False
        
