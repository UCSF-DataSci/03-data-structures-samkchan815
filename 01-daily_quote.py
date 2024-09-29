#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

import random
from datetime import date


quotes = [
    # Create a list of quotes here
    "You will be found",
    "No day but today", 
    "No one deserves to disappear",
    "It's just life, so keep dancing through",
    "Forget regret, or life is yours to miss",
    "We control one flat rectangle of canvas at a time",
    
]

def get_quote_of_the_day(quotes):
    '''Return a random quote of the day from list'''
    todays_quote = None

    # Your code here
    todays_quote = random.choice(quotes) # get random quote
    return todays_quote # return random quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Add to Cron using the following:
print('0 8 * * * /usr/bin/python3 ./01-daily_quote.py >> output.txt')

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3 /path/to/quote_generator.py >> /path/to/daily_quote.txt

