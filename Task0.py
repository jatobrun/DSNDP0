"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from time import time
def count_elapsed_time(f):
    """
    Decorator.
    Execute the function and calculate the elapsed time.
    Print the result to the standard output.
    """
    def wrapper():
        # Start counting.
        start_time = time()
        # Take the original function's return value.
        ret = f()
        # Calculate the elapsed time.
        elapsed_time = time() - start_time
        print("Elapsed time: %0.10f seconds." % elapsed_time)
        return ret
    
    return wrapper

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
@count_elapsed_time
def task0():
    print(f'First record of texts, {texts[0][1]} text {texts[0][1]} at time {texts[0][2]}')
    print(f'Last record of calls, {calls[-1][1]} calls {calls[-1][0]} at time {calls[-1][2]}, lasting {calls[-1][3]} seconds')

@count_elapsed_time
def task1():
    first_record_text = texts[0]
    last_record_calls = calls[-1]
    print(f'First record of texts, {first_record_text[1]} text {first_record_text[1]} at time {first_record_text[2]}')
    print(f'Last record of calls, {last_record_calls[1]} calls {last_record_calls[0]} at time {last_record_calls[2]}, lasting {last_record_calls[3]} seconds')

task0()
task1()