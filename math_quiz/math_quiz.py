import random                                # Importing the package random


def Rand_int_generator(min, max):            # Defining a function which returns a random integer between min and max
    """ 
    Generates a Random integer.
    """
    return random.randint(min, max)


def Rand_operator_generator():                # Defining a function which returns a random choice of operators i.e. '+', '-', '*'
    """
    Generates a Random operator.
    """
    return random.choice(['+', '-', '*'])


def Operation_generator(n1, n2, o):           # Defining a function which defines some operations according to the choice of operators i.e. '+', '-', '*'and returns p and a
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 - n2
    elif o == '-': a = n1 + n2
    else: a = n1 * n2
    return p, a

def math_quiz():                              # Defining a function called math_quiz() which contains the main code for our math quiz game
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = Rand_int_generator(1, 10); n2 = Rand_int_generator(1, 5.5); o = Rand_operator_generator()

        PROBLEM, ANSWER = Operation_generator(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            if type(useranswer) == int || float
        except:
            print("Enter a valid number")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
