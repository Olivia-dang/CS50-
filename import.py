import csv

from cs50 import get_string


with open('phonebook.csv', 'a') as phonefile:
    name = get_string('Name: ')
    number = get_string('Number:')
        
    #write the name and number to csv
    writer = csv.writer(phonefile)  #csv: library imported above, 
        
    writer.writerow([name,number])

