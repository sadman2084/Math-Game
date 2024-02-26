import random
import time
OPERATORS = ["+", "-", "*"]
MIN_OPARAND = 3
MAX_OPARAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPARAND, MAX_OPARAND)
    right = random.randint(MIN_OPARAND, MAX_OPARAND)
    operator = random.choice(OPERATORS)  ###Randomly choose operator from OPERATORS

    expr = str(left) + " " + operator + " " + str(right)
    # to evaluate the mathematical expression generated in the generate_problem() function.
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("--------------------------------")

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()

    while True:
        guess = input("problem #" + str(i + 1) + ":" + expr + "=")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time
print("--------------------------------")
print("Nice work,You finished in", total_time, " seconds!")
