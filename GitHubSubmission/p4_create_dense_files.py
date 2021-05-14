#there are three sample files for inputs, test1 and test2 and test3: value will be 1, 2 or 3.
test_case = int(input('please give me a test case number, 1, 2 or 3:'))
# Following are the output files created by this program. These have one line for every month
annuity_terms_filename = 'p4_test%d_terms.csv' % test_case
sparse_rates_filename = 'p4_test%d_interest_rates.csv' % test_case
sparse_cf_filename = 'p4_test%d_cash_flows.csv' % test_case
# Get the annuity terms
terms_file = open(annuity_terms_filename, 'r')
terms_file.readline()  # skip the first line of column titles
line = terms_file.readline()  # this is the line with the numbers, e.g., '120,3.0'
annuity_term, inflation = line.split(',')  # split into our two values (as strings), e.g., '120', '3.0'
annuity_term = int(annuity_term)  # convert to an integer from a string
inflation = float(inflation) / 100.0  # convert to a float and ratio from a string with percent number
terms_file.close()
#use sparse files to create new file:
sparse_fileIR = open(sparse_rates_filename, 'r')
dense_fileIR = open('p4_test%d_dense_rates_JG' % test_case, 'w')
month = 1
prev = 0
for line in sparse_fileIR:
    IR_month, IR_amount = line.split(',')
    IR_month = int(IR_month)  # convert the string IR_month into an integer
    IR_amount = float(IR_amount)  # convert the string IR_amount into a float
    #prev = IR_amount
    while month < IR_month: #going through the sparse file, replacing 0s with prev value, and valid values placed in corresponding month. 
        dense_fileIR.write(str(prev) + '\n')  # Needs To Be the IR of the previous month!!!!
        month += 1
    dense_fileIR.write(str(IR_amount) + '\n') # here's the IR month
    prev = IR_amount#
    month += 1
while month <= annuity_term:  #  rest of terms till end of annuity
    dense_fileIR.write(str(prev) + '\n') #  Needs To Be the IR of the previous month!!!!
    month += 1

sparse_fileIR.close()
dense_fileIR.close()
#Now move onto the files for Cash Flow Dense!
sparse_fileCF = open(sparse_cf_filename, 'r')
dense_fileCF = open('p4_test%d_dense_cf_JG' % test_case, 'w')
month = 1
for line in sparse_fileCF:
    cf_month, cf_amount = line.split(',')
    cf_month = int(cf_month)  # convert the string cf_month into an integer
    cf_amount = float(cf_amount)  # convert the string cf_amount into a float
    print(cf_month) #test print
    print(cf_amount) #test print
    while month < cf_month:
        dense_fileCF.write(str(0.0) + '\n')  # no cash flows for this month
        month += 1
    dense_fileCF.write(str(cf_amount) + '\n') # here's the cash flow month
    month += 1
while month <= annuity_term:  # any later months until the end of the annuity term after last cash flow
    dense_fileCF.write(str(0.0) + '\n')
    month += 1
dense_fileCF.close()
sparse_fileCF.close()
print('done')
#works and matches test 1 restults for both IR and CF! 
