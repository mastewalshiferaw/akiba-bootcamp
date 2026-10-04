Destination = input("What is your Destination: ")
distance_km = float(input("Distance in km: "))
avg_speed = float(input("Average speed in km/hr: "))

time = distance_km/avg_speed
time_sec = (distance_km/avg_speed)*3600
print(f"Estimated Travel Time(in hours): {time}hours")
print(f"Estimated Travel Time (in seconds): {time_sec}seconds")