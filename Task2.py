"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import operator
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def task2(calls):
    telephone_numbers = {}
    for e in calls:
        if e[0] in telephone_numbers:
            telephone_numbers[e[0]] += int(e[-1])
        else:
            telephone_numbers[e[0]] = int(e[-1])
        
        if e[1] in telephone_numbers:
            telephone_numbers[e[1]] += int(e[-1])
        else:
            telephone_numbers[e[1]] = int(e[-1])
    max_numer = max(telephone_numbers.items(), key=operator.itemgetter(1))[0]
    print(f'''{max_numer} spent the longest time {telephone_numbers[max_numer]} seconds on the phone during September 2016''')
         
task2(calls)