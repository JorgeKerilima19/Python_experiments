
lst={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}

number="XVII"

def roman_to_int(num):
    num=num.upper()
    integer=0
    try:
        for i in range(len(num)):
            if num[i] in lst:

                if i+1<len(num) and lst[num[i]]<lst[num[i+1]]:
                    integer-=lst[num[i]]
                else:
                    integer+=lst[num[i]]

    except KeyError:
        print(f"the {num[i+1]} is not part of the Roman numeric system")
        exit()
    return integer
print(roman_to_int(number))


lt=[["I",1],["VI",4],["V",5],["IX",9],["X",10],
    ["XL",40],["L",50],["XC",90],["C",100],["CD",400],["D",500],
    ["CM",900],["M",1000],]

nunbr=129
def int_to_roman(num):
    roman=""
    for sym, val in reversed(lt):
        if num//val:
            count=num//val
            roman+=(sym*count)
            num=num%val
    return roman

print(int_to_roman(nunbr))