# put your python code here
duration = int(input())
food_cost = int(input())
flight_cost = int(input())
hotel_night = int(input())

print(food_cost * duration + flight_cost * 2 + hotel_night * (duration - 1))
