# put your python code here
group1 = int(input())
group2 = int(input())
group3 = int(input())

desk1 = group1 // 2 + group1 % 2
desk2 = group2 // 2 + group2 % 2
desk3 = group3 // 2 + group3 % 2

total_desks = desk1 + desk2 + desk3
print(total_desks)
