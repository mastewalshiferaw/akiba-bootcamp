Destination = input("What is your Destination: ")
distance_km = float(input("Distance in km: "))
avg_speed = float(input("Average speed in km/hr: "))

time = distance_km/avg_speed

print(f"Estimated Travel Time(in hours): {time}")
