order_total = 1000

if order_total < 45:
    discount = 0

else:
    discount = 45

#could be written as 
discount = 25 if order_total > 45 else 0

print(discount)