year1 = int(input('Enter the year for date 1 (yyyy): '))
month1 = int(input('Enter the month for date 1 (mm): '))
day1 = int(input('Enter the day for date 1 (dd): '))
year2 = int(input('Enter the year for date 2 (yyyy): '))
month2 = int(input('Enter the month for date 2 (mm): '))
day2 = int(input('Enter the day for date 2 (dd): '))

years = (year1 - year2) * 360
months = (month1 - month2) * 30
days = (day1 - day2)

difference = years + months + days
out = print(f'The difference between {month1}/{day1}/{year1} and {month2}/{day2}/{year2} is {abs(difference)} days!')
