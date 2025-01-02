print ("welcome to tip calculator")
bill = float(input("what was the total bill?\t"))
people = float(input("how many people to split the bill\t"))
percentage = float(input("what percentage would you like to tip?\t"))
percentage_of_bill = (percentage/100) * bill
net_bill = bill + percentage_of_bill
split = net_bill/people
print ("Each person should pay: $",split)
