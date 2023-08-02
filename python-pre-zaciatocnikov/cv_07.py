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
#ÚLOHA 4
#ÚLOHA 5

