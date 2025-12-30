# Topic: Daily Temperature & Rainfall Observation

# Location details
location = "Green Valley"
season = "Monsoon"

print("Location:", location)
print("Season:", season)

# Temperature data (in Celsius) for 7 days
temperatures = [28, 29, 27, 26, 30, 31, 29]

# Rainfall data (in mm) for 7 days
rainfall = [12, 18, 25, 40, 10, 5, 15]

# Number of days
days = len(temperatures)

# Calculations
avg_temp = sum(temperatures) / days
avg_rainfall = sum(rainfall) / days
max_temp = max(temperatures)
min_temp = min(temperatures)
total_rainfall = sum(rainfall)

# Results
print("\n--- Weekly Weather Summary ---")
print("Average Temperature:", avg_temp, "°C")
print("Maximum Temperature:", max_temp, "°C")
print("Minimum Temperature:", min_temp, "°C")
print("Average Rainfall:", avg_rainfall, "mm")
print("Total Rainfall:", total_rainfall, "mm")

# Simple condition analysis
if avg_rainfall > 20:
    print("Weather Insight: Heavy rainfall week 🌧️")
else:
    print("Weather Insight: Moderate rainfall 🌦️")
  
if avg_temp > 30:
    print("Temperature Status: Hot week 🔥")
else:
    print("Temperature Status: Pleasant weather 🌿")
