#if applicant has high income AND good credit then eligible for loan

high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for loan")

else:
    print("Not eligible for loan")



#if applicant has high income OR good credit then eligible for loan

high_income = True
good_credit = False

if high_income or good_credit:
    print("Eligible for loan")

else:
    print("Not eligible for loan")


#AND : both
#OR : EITHER 1
#NOT :

#if applicant has good credit AND doesnt have a criminal record then eligible for a loan

high_income = True
has_criminal_record = True

if high_income and not has_criminal_record:
    print("Eligible for loan")

else:
    print("Not eligible for loan")
