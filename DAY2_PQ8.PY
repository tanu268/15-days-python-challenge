# Input: Number of minutes
minutes = int(input("Enter the number of minutes: "))

# Convert minutes to hours and remaining minutes
hours = minutes // 60  # Get the whole number of hours
remaining_minutes = minutes % 60  # Get the remaining minutes

# Display the result
print(f"{minutes} minutes = {hours} hour(s) and {remaining_minutes} minute(s)")
