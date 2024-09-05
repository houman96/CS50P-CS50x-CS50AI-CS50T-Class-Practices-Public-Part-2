def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    newd = float(d.replace("$",""))
    return newd


def percent_to_float(p):
    newp = float(p.replace("%",""))
    percentp = newp / 100
    return percentp

main()
