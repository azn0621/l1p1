field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110
total =  field1 + field2 + field3 + field4 + field5
average = total / 5 
print("total harvest:", total, "kg")
print("average per field:", average, "kg")
price_per_kg = 15
earnings = total * price_per_kg
print("total learnings: RS.", earnings)
bags = total // 25
leftover = total % 25
print("full bags packed:", bags)
print("leftover grain:", leftover, "kg" )
