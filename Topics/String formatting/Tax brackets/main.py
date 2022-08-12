income = int(input())

if 0 <= income <= 15527:
    percent = 0
    calculated_tax = round(percent * income / 100)
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
elif 15528 <= income <= 42707:
    percent = 15
    calculated_tax = round(percent * income / 100)
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
elif 42708 <= income <= 132406:
    percent = 25
    calculated_tax = round(percent * income / 100)
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
else:
    percent = 28
    calculated_tax = round(percent * income / 100)
    print(f"The tax for {income} is {percent}%. That is {calculated_tax} dollars!")
