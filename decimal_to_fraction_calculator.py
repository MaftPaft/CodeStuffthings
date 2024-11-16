"""
returns the simplified fraction from a decimal. Idk why this would be useful, but calculators do this so ima do it too tyshi.
"""
# decmial library to avoid Binary Issues
from decimal import Decimal

# Citation for finding Greatest common divisor efficiently
#https://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
def GCD(a,b):
    # j is always bigger than k
    j=a if a>=b else b
    k=b if j==a else a
    # recalculates j as k, and k as the remainder of jk iteratively, until k is equal to zero.
    while k!=0:
        j,k=(k,j%k)
    return j

# To simplify fractions
def simplify(a,b):
    CommonDivisor=GCD(a,b)
    return [a//CommonDivisor,b//CommonDivisor]

def float_to_fraction(numf: float):
    # if the number is a decimal
    if numf%1==0: return [f"{numf}/1",numf]
    # using the decimal libray to avoid Binary Issues
    numf=Decimal(str(numf))
    # 10 to the power of the length of numbers in the decimal to get the denominator
    denom=10**len(str(numf).split(".")[1])
    
    # multiplied the original number and denominator to get the numerator
    num=int(numf*denom)
    # simplifying the fraction
    a,b=simplify(num,denom)
    return [f"{a}/{b}",a/b]

from random import uniform

n=uniform(1,100)
fn=float_to_fraction(n)
print(f"number: {n}, \n\n[fraction, divided_fraction]: {fn} \n\n the divided_fraction should equal the number given")

#  the divided_fraction should equal the number given
# TEST CASE OUTPUT:
# number: 89.80411283034455, 

# [fraction, divided_fraction]: ['1796082256606891/20000000000000', 89.80411283034455] 


# number: 9966.525918933903, 

# [fraction, divided_fraction]: ['9966525918933903/1000000000000', 9966.525918933903]
