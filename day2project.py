#cNamw of the project 
print('Welcome to the ctip calculator!')
#The total bill
bill=float(input('What is the total bill? $'))
#The tip to be given
tip=int(input('How much tip would you like to give? 10,12,or 15? '))
#The number of people to share the bill
people=int(input('How many people will split the bill?'))
#Calculation of the bill tip
bill_tip=tip/100*bill+bill
# The bill tip per person
bill_tip_per_person=bill_tip/people
# rounding off the finall amount to be apid by each person
#final_amount=round(bill_tip_per_person,2) 
#another method of rounding
final_amount="{:.2f}".format(bill_tip_per_person)
# Then lastly printing the result using formatted string
print(f"Each person should pay: ${final_amount}")
#print("Each person should pay $ {}".format(final_amount))





#https://www.canva.com/design/DAFCTvJeDFY/7opypo4KmVaiB-HXRkrq9w/edit?utm_content=DAFCTvJeDFY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
#print(type(bill))