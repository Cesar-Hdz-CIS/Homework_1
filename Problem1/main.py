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

if Curr_Day == Birth_Day and Curr_Month == Birth_Month:
    print('Happy Birthday!')