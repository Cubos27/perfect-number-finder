print("Number finder")
max_perfect_nums = int(input("Enter how many perfect numbers to show: "))
# Un número perfecto es un número entero positivo que es igual a la suma de sus 
# divisores propios positivos excluyéndose a sí mismo.

perfect_numbers_found = 0
number = 0
perfect_numbers = []
while perfect_numbers_found < max_perfect_nums:
    number += 1
    divisors = []
    for i in range(1, number):
        if (number % i) == 0:
            divisors.append(i)
    print(f"number: {number}\ndivisors: {divisors}")
    if sum(divisors) == number:
        perfect_numbers.append(number)
        perfect_numbers_found += 1
print("Perfect numbers:")
print(perfect_numbers)