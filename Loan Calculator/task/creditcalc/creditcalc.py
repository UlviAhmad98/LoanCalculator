import argparse
import math
# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'

# # write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

# print("Enter the loan principal:")
# principal = int(input())
# print("What do you want to calculate?")
# print('type "m" - for number of monthly payments,')
# print('type "p" - for the monthly payment:')

# answer = input()
# if answer == "m":
#     print("Enter the monthly payment:")
#     payment = int(input())
#     months = math.ceil(principal / payment)
#     if months == 1:
#         #print("")
#         print(f"It will take {months} month to repay the loan")
#     else:
#         #print("")
#         print(f"It will take {months} months to repay the loan")

# elif answer == "p":
#     print("Enter the number of months:")
#     months = int(input())
#     payment = math.ceil(principal / months)
#     last_payment = principal - (months - 1) * payment
#     if last_payment == payment:
#         print(f"Your monthly payment = {payment}")
#     else:
#         print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
#
# print("What do you want to calculate?")
# print('type "n" for number of monthly payments,')
# print('type "a" for annuity monthly payment amount,')
# print('type "p" for loan principal:')
# answer = input()
# if answer == "n":
#     print("Enter the loan principal:")
#     P = int(input())
#     print("Enter the monthly payment:")
#     A = float(input())
#     print("Enter the loan interest:")
#     loan_interest = float(input())
#     i = loan_interest / (12 * 100)
#     n = math.ceil(math.log(A / (A - i * P), 1 + i))
#     year = int(n // 12)
#     month = int(n % 12)
#     if year == 0 and month == 1:
#         print(f"It will take {month} month to repay this loan!")
#     elif year == 1 and month == 0:
#         print(f"It will take {year} year to repay this loan!")
#     elif year == 0 and 1 < month <= 11:
#         print(f"It will take {month} months to repay this loan!")
#     elif year == 1 and month == 1:
#         print(f"It will take {year} year and {month} month to repay this loan!")
#     elif year == 1 and 1 < month <= 11:
#         print(f"It will take {year} year and {month} months to repay this loan!")
#     elif year >= 1 and month == 1:
#         print(f"It will take {year} years and {month} month to repay this loan!")
#     else:
#         print(f"It will take {year} years and {month} months to repay this loan!")
# elif answer == "a":
#     print("Enter the loan principal:")
#     P = int(input())
#     print("Enter the number of periods:")
#     n = int(input())
#     print("Enter the loan interest:")
#     loan_interest = float(input())
#     i = loan_interest / (12 * 100)
#     A = math.ceil(P * i * pow((1 + i), n) / (pow((1 + i), n) - 1))
#     print(f"Your monthly payment = {A}!")
# elif answer == "p":
#     print("Enter the annuity payment:")
#     A = float(input())
#     print("Enter the number of periods:")
#     n = int(input())
#     print("Enter the loan interest:")
#     loan_interest = float(input())
#     i = loan_interest / (12 * 100)
#     P = math.floor(A / (i * pow((1 + i), n) / (pow((1 + i), n) - 1)))
#     print(f"Your loan principal - {P}!")
#

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])

parser.add_argument("--principal", type=int)

parser.add_argument("--periods", type=int)

parser.add_argument("--interest", type=float)

parser.add_argument("--payment", type=int)

args = parser.parse_args()

payment_type = args.type
P = args.principal
n = args.periods
interest = args.interest
A = args.payment

paid = []
alist = []

for arg in vars(args):
    if getattr(args, arg) is not None:
        alist.append(getattr(args, arg))

# or (type == "diff" and monthly_payment is True)

if len(alist) != 4 or interest is None or payment_type not in ("annuity", "diff"):
    print("Incorrect parameters")
else:
    if payment_type == "diff" and A is not None:
        print("Incorrect parameters")
    elif payment_type == "diff":
        for m in range(1, n + 1):
            i = interest / 12 * 100
            D = round(P / n + i * (P - (P * (m - 1)) / n))
            paid += D
            print(f"Month {m}: payment is {D}")
            print("")
        overpayment = abs(P - sum(paid))
        print(f"Overpayment = {overpayment}")

    elif payment_type == "annuity":
        if A is True and P is True and interest is True:
            i = interest / 12 * 100
            n = math.ceil(math.log(A / (A - i * P), 1 + i))
            year = int(n // 12)
            month = int(n % 12)
            if year == 0 and month == 1:
                print(f"It will take {month} month to repay this loan!")
            elif year == 1 and month == 0:
                print(f"It will take {year} year to repay this loan!")
            elif year == 0 and 1 < month <= 11:
                print(f"It will take {month} months to repay this loan!")
            elif year == 1 and month == 1:
                print(f"It will take {year} year and {month} month to repay this loan!")
            elif year == 1 and 1 < month <= 11:
                print(f"It will take {year} year and {month} months to repay this loan!")
            elif year >= 1 and month == 1:
                print(f"It will take {year} years and {month} month to repay this loan!")
            else:
                print(f"It will take {year} years and {month} months to repay this loan!")
            overpayment = abs(P - (A * n))
            print(f"Overpayment = {overpayment}")
        elif A is True and n is True and interest is True:
            i = interest / 12 * 100
            P = math.floor(A / (i * pow((1 + i), n) / (pow((1 + i), n) - 1)))
            print(f"Your loan principal = {P}!")
            overpayment = abs(P - (A * n))
            print(f"Overpayment = {overpayment}")
