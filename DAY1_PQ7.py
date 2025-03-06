#Write a program that converts a given number of days into years, weeks, and days


days = int(input("Enter the number of days: "))

years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7
days_left = remaining_days % 7

print(f"{days} days = {years} years, {weeks} weeks, and {days_left} days")
