import turtle
#ÚLOHA 1
def list_all_divisors(number):
    divisors = [str(divisor) for divisor in range(1, number + 1) if number % divisor == 0]
    print(" ".join(divisors))

# Testovanie funkcie
list_all_divisors(24)
#1 2 3 4 6 8 12 24

#ÚLOHA 2
def list_all_divisors(number):
    divisors = [divisor for divisor in range(1, number) if number % divisor == 0]
    return divisors

def is_perfect(number):
    divisors = list_all_divisors(number)
    sum_of_divisors = sum(divisors)
    return sum_of_divisors == number

# Testovanie funkcie
print(is_perfect(6))  # True
print(is_perfect(24))  # False
print(is_perfect(12))  # False


#ÚLOHA 3

import turtle

def ball(x, y, r):
    turtle.penup()
    turtle.goto(x, y - r)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def snowman(x, y, r):
    ball(x, y, r)
    ball(x, y + (2 * r // 3), 2 * r // 3)
    ball(x, y + (4 * r // 3), r // 3)

# Test
turtle.speed(1)
turtle.bgcolor("lightblue")
snowman(150, 400, 90)
snowman(400, 300, 45)
snowman(100, 200, 30)
turtle.done()



#ÚLOHA 4

def transform(dictonary):
    return [(key, value) for key, value in dictonary.items()]

#Test
A = {'meno' : "Zdena Studenková", 'vek' : "nedefinované"}
prevod = transform(A)
print(prevod)

#ÚLOHA 5

def merge(A,B):
    merged_dict = A.copy()
    for key, value in B.items():
        if key in merged_dict:
            merged_dict[key] = [merged_dict[key], value]
        else:
            merged_dict[key] = value
    return merged_dict

#Test

dict_A = {1: "one", 2: "two"}
dict_B = {2: "dva", 3: "three"}
result = merge(dict_A, dict_B)
print(result)
