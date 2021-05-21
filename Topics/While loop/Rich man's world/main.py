deposit = int(input())
interest_rate = 1.071
number_of_years = 0

while deposit <= 700000:
    deposit *= interest_rate
    number_of_years += 1
print(number_of_years)
