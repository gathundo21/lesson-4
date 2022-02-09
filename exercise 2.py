eng=int(input("score: "))
math=int(input("score: "))
phyc=int(input("score: "))
chem=int(input("score: "))
kisw=int(input("score: "))


average=(eng+math+phyc+chem+kisw)/5

if average>=70 and average<=100:
    print("grade A")
elif average>=60 and average<=69:
    print("grade B")
elif average>=50 and average<=59:
    print("grade C")
elif average>=40 and average<=49:
    print("grade D")
elif average>=0 and average<=39:
    print("Fail")
else:
    print("invalid")