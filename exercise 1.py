salary=int(input("enter salary"))
years=int(input("enter years"))
if years>10:
    print(0.1*salary)
elif  years>=6 and years<=10:

    print(0.08*salary)

elif  years<6:
    print(0.05*salary)
