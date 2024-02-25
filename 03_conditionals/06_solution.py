# Problem: Choose a mode of transportation based on the distance
# (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

# get the destination distance and convert it to integer
destination_distance = input("Please provide distance of your destination in KM : ")
distance_in_int = int(destination_distance)

# suggest mode of transport based on destination distance
if distance_in_int < 3:
    transport = "Walk"

elif distance_in_int <= 15:
    transport = "Bike"

else:
    transport = "Car"

print("Recommended way of transport is -",transport)