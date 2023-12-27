"""
Author: Diyorbek Ibragimov
Andrew ID: dibragim
Date: December 27, 2023
"""

def solution():
    N = int(input())
    secretWord = input()

    # feedbacks will already contain "*****" since secret word is 
    # guaranteed to be in the list of all guessed words
    feedbacks = {
        "*****": 1,
    }
    for _ in range(N-1):
        guess = input()
        feedback = ""
        # the length of the guessed word is always constant and equals to 5
        for i in range(5): # O(1)
            if guess[i] in secretWord: # O(1) 
                # since the length of the secret word is always 5
                if guess[i] == secretWord[i]:
                    # the letter is in the same position
                    # both in the guessed word and the secret word
                    # so the feedback generated is "*"
                    feedback += "*"
                else:
                    # the letter is in the secret word
                    # but in the wrong position
                    # so the feedback generated is "!"
                    feedback += "!"
            else:
                # the letter is not in the secret word
                # so the feedback generated is "X"
                feedback += "X"
        
        # checking if the feedback generated is in the dictionary
        # of all the feedbacks for every word
        # since it is possible that two or more words
        # can have the same feedback
        if feedback in feedbacks:
            feedbacks[feedback] += 1
        else:
            feedbacks[feedback] = 1
    
    G = int(input())
    for _ in range(G):
        feedback = input()
        print(feedbacks[feedback])

if __name__ == "__main__":
    solution()