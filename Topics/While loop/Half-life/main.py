initial_quantity = int(input())
final_quantity = int(input())

number_of_atoms = initial_quantity
half_life = 0

while number_of_atoms > final_quantity:
    number_of_atoms /= 2
    half_life += 1
print(half_life * 12)
