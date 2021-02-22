from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change > 0:
        break

        
cents = int(round(change*100))
count =0

while cents>0:
    while cents>=25:
        count +=1
        cents -=25
    while cents >=10:
        count +=1
        cents -=10
    while cents >=5:
        count +=1
        cents -=5
    while cents >=1:
        count +=1
        cents -=1

print(count)