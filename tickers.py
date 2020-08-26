import re
import time

# test

# get input from terminal for debugging
print('for company input c; for ticker input t')
# make sure valid input
switch_check = True
while switch_check:
    switch = input('company or ticker').lower()
    if switch == 'c' or switch == 't':
        switch_check = False
    else:
        print('Try again, for company input c; for ticker input t')

    



if switch == 'c':
    find_comp(input('what company? '))
else:
    find_tick(input('what ticker? '))

# starting from a ticker
# swapping characters
# fat finger errors -> need to find a way to reference close letters on keyboard
# double character (aapl v appl)
def find_tick(ticker):
    ticker = ticker.lower()
    out = []
    
    # if len = 4, swap middle 2
    if len(ticker) == 4:
        swap = ticker[0]+ticker[2]+ticker[1]+ticker[3]
        if check_tick(swap):
            out.append(swap)    
    
    # get company name, if short check that
    cname = get_comp_name(ticker)
    check_comp_name(cname, ticker)
             
def find_comp(comp):
     
        
def check_tick (tick):
    # something in finance api, if get that it exists, true
    
def check_comp_name(company, ticker):
    company = company.lower()
    ticker = ticker.lower()
    out = []
    # len of name
    
    # split name, try first word
    words = company.split()
    for word in words:
        if len(word) <= 4 and word != ticker:
            if check_tick(word):
                out.append(word)
            
        
    # try initials 
                 
    # check list against known tickers  
    