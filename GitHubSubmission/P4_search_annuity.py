from math import e
test_case = 1#adjust in order to see other outputs for other test cases.
annuity_terms_filename = 'p4_test%d_terms.csv' % test_case
sparse_cf_filename = 'p4_test%d_cash_flows.csv' % test_case
sparse_rates_filename = 'p4_test%d_interest_rates.csv' % test_case

# Get the annuity terms
terms_file = open(annuity_terms_filename, 'r')
terms_file.readline()  # skip the first line of column titles
line = terms_file.readline()  # this is the line with the numbers, e.g., '120,3.0'
annuity_term, inflation = line.split(',')  # split into our two values (as strings), e.g., '120', '3.0'
annuity_term = int(annuity_term)  # convert to an integer from a string
inflation = float(inflation) / 100.0  # convert to a float and ratio from a string with percent number
terms_file.close()
### End of section you want to paste into your programs
test_case = 1
total = 0.0
cf_npv = 0.0
cf_file = open('p4_test%d_dense_cf_JG' % test_case, 'r')
rates_file = open('p4_test%d_dense_rates_JG' % test_case, 'r')
months = 1
for cf_line, rate_line in zip(cf_file, rates_file):
    rate = float(rate_line) / 12.0 / 100.0
    cash_flow = float(cf_line)
    total += cash_flow
    cf_npv += cash_flow * e ** (-rate * months)
    months += 1
cf_file.close()
print('Total customer-provided cash flows: $%.2f' % total)
print('NPV of customer-provided cash flows: $%.2f' % cf_npv)
lo = 0.0
hi = total #$92088.12
# Now we have a low that is too low and a high that is too high, so we can use bisection search
print('\nSearching for correct beginning monthly annuity payment:')
last_guess = lo #0
guess = hi  # which we will change to (lo + hi) / 2 in the loop
iter_count = 1  #used to count bisection iterations### End of verbatim code
total = 0.0
init_cf_npv = cf_npv #using this as a place holder variable to hold onto the values for the original cf_npv
#---------------------------------------------------------------------------------------work on below
cf_file = open('p4_test%d_dense_cf_JG' % test_case, 'r')
rates_file = open('p4_test%d_dense_rates_JG' % test_case, 'r')
months = 1
guess = (lo + hi) / 2
while guess != last_guess:#condition matching for when the system has finished bisection
    cf_npv = init_cf_npv
    months = 1
    last_guess = guess
    guess = round(guess, 2)
    npv = cf_npv#which from the print above is 90232.81
    payment = -guess
    #print('payment is:', payment)#useful for debugging
    #payment = -46044.06
    cf_file = open('p4_test%d_dense_cf_JG' % test_case, 'r')
    rates_file = open('p4_test%d_dense_rates_JG' % test_case, 'r')#gathering the read in data from my precreated files
    #cf_file = open('p4_test1_dense_cf.txt')delete
    #rates_file = open('p4_test1_dense_rates.txt') delete
    #print('is it 90232.81?:', cf_npv)#useful for debugging
    for cf_line, rate_line in zip(cf_file, rates_file):
        #print(payment, months)we know that this is working
        rate = float(rate_line) / 12.0 / 100.0
        total += payment
        cf_npv += payment * e ** (-rate * months)
        #print('the payment we used:', payment, months, cf_npv) #super duper useful for debugging
        if months % 12 == 0:
            payment += round(payment * inflation, 2)#is this in the right order?
        months += 1
    paid = (lo + hi)/2
    mix = float("%.2f" %(lo + hi))
    #print('NPV of cash flows: $%.2f' % cf_npv) useful for debugging
    print(iter_count, ':With annuity of (', mix,')/2 = $%.2f' % paid, 'NPV is: $%.2f' % cf_npv)
    cf_file.close()
    rates_file.close()#close and reopen files each time
  #--------------------------------------------------------------------------------------  this line devides the guess adjustment and NPV calc. 
    npv = cf_npv
    if npv < 0.0:
        hi = guess
    else:
        lo = guess
    iter_count += 1
    guess = (lo + hi) / 2
    

print(iter_count, ':With annuity of (', mix,')/2 = $%.2f' % paid, 'NPV is: $%.2f' % cf_npv)#final print statement
print("\n")#gap
payment = float("%.2f" %(paid))    
payment2= float("%.2f" %(payment* 1.009999))
payment3= float("%.2f" %(payment2* 1.009999))
total_pay = float("%.2f" %(payment*12 + payment2*12 + payment3*2))
print('First year pay $', payment,'per month')
print('next year pay $', payment2,'per month')
print('next year pay $', payment3,'per month')
print('for a total of $', total_pay)#the sum of 12 months on payment1, 12 months of payment2 and 2 months on payment3.
