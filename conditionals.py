# late = False

# if late:
#     print("I will call my manager")
# else:
#     print("No need to call my manager")


income = 150000

if income < 10000:
    tax_coefficient= 0

elif income < 30000:
    tax_coefficient = 0.2

elif income < 100000:
    tax_coefficient =0.35

else:
    tax_coefficient = 0.45

print(f"You will pay {tax_coefficient *income} in taxes")