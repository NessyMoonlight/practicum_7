import math

def min_questions(n):
    return math.ceil(math.log2(n))

n = int(input())
min_questions = min_questions(n)
print(min_questions)