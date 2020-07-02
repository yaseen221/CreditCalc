import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", help="Annuity ('annuity') or Differentiated ('diff')")
parser.add_argument("--principal", help="Credit Principal", type=float)
parser.add_argument("--payment", help="Monthly Payment", type=float)
parser.add_argument("--periods", help="No. of periods(months)", type=int)
parser.add_argument("--interest", help="Rate of interest", type=float)

args = parser.parse_args()
sys_args = sys.argv

credit_type = args.type
principal = args.principal
payment = args.payment
months = args.periods
interest = args.interest


def calculate_months():
    i = (interest / (12 * 100))
    k = payment / (payment - (i * principal))
    n = math.ceil(math.log(k, 1+i))
    if n > 12:
        if n % 12 != 0:
            print(f"You need {n // 12} years and {n % 12} months to repay this credit!")
        elif n % 12 == 0:
            print(f"You need {n // 12} years to repay this credit!")
        else:
            print(f"You need {n % 12} months to repay this credit!")
    print("Overpayment =", math.ceil((payment * n) - principal))


def calculate_principal():
    i = (interest / (12 * 100))
    credit_principal = payment / ((i * ((1 + i) ** months)) / (((1 + i) ** months) - 1))
    print(f"Your credit principal = {int(credit_principal)}!")
    print("Overpayment =", math.ceil((payment * months) - credit_principal))


def calculate_annuity_payment():
    i = (interest / (12 * 100))
    annuity_payment = math.ceil(principal * ((i * math.pow((1+i), months)) / (math.pow((1+i), months) - 1)))
    print(f"Your annuity payment = {annuity_payment}!")
    print("Overpayment =", math.ceil((annuity_payment * months) - principal))


def calculate_diff_payments():
    d_m = []
    i = (interest / (12 * 100))
    for j in range(1, months+1):
        d_m.append(math.ceil((principal/months) + (i * (principal - ((principal * (j-1))/months)))))
        print(f"Month {j}: paid out {d_m[j-1]}")
    print("Overpayment = ", math.ceil(sum(d_m)-principal))


if len(sys_args) <= 4:
    print("Incorrect parameters")

else:
    if credit_type == "annuity":
        if args.payment and args.principal and args.interest:
            if (args.payment > 0) and (args.principal > 0) and (args.interest > 0):
                calculate_months()
            else:
                print("Incorrect parameters")

        elif args.payment and args.periods and args.interest:
            if (args.payment > 0) and (args.periods > 0) and (args.interest > 0):
                calculate_principal()
            else:
                print("Incorrect parameters")

        elif args.principal and args.periods and args.interest:
            if (args.principal > 0) and (args.periods > 0) and (args.interest > 0):
                calculate_annuity_payment()
            else:
                print("Incorrect parameters")

    elif credit_type == "diff":
        if args.principal and args.periods and args.interest and (not args.payment):
            if (args.principal > 0) and (args.periods > 0) and (args.interest > 0):
                calculate_diff_payments()
        else:
            print("Incorrect parameters")

    else:
        print("Incorrect parameters")
