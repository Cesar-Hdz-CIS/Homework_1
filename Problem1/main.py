# Cesar Hernandez 1835494

print('Birthday Calculator')
print('Current Day')
Curr_Month = int(input("Month: "))
Curr_Day = int(input('Day: '))
Curr_Year = int(input('Year: '))
print('Birthday')
Birth_Month = int(input('Month: '))
Birth_Day = int(input('Day: '))
Birth_Year = int(input('Year: '))

Years = Curr_Year - Birth_Year - 1

if Birth_Month < Curr_Month:
    Years += 1
elif Curr_Month == Birth_Month:
    if Birth_Day <= Curr_Day:
        Years += 1

print('You are', Years, 'old.')

if Curr_Day == Birth_Day and Curr_Month == Birth_Month:
    print('Happy Birthday!')