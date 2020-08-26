import re
import time
# get input from terminal for debugging

print('for company input c; for ticker input t')
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
    find_tick(input('what ticker?'))


def find_tick(ticker):
    out = []
    
    # if len = 4, swap middle 2
    if len(ticker) == 4:
        swap = t[0]+t[2]+t[1]+t[3]
        if check_tick(swap):
            out.append(swap)    
    
    # get company name, if short check that
    cname = get_comp_name(ticker)
    check_comp_name(cname, ticker)
             
def find_comp(comp):
     
        
def check_tick (tick):
    # something in finance api, if get that it exists, true
    
def check_comp_name(company, ticker):
    # len of name
    
    # split name, try first word
    
    # try initials 
                 
    # check list against known tickers  
    