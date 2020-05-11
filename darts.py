from math import sqrt
import sys

def score(x, y):
    """
    Given a landing point for a dart, return the score earned.
    """
    distance = sqrt(x * x + y * y)
    if distance > 10:
        return 0
    if distance > 5:
        return 1
    if distance > 1:
        return 5
    return 10

if __name__ == '__main__':
    print("Welcome to darts game")
    x = input("Enter X value")
    y = input("Enter Y value")
    score = score(x, y)
    print("You scored: %d" % score)