import math
import sys

def CalculateTotalPrice(price,tax_rate):
    total=price+price*tax_rate
    return total

def process_data(data):
    if data>0:
        print("Positive number:",data)
    else:
        print("Non-positive:",data)
    return data

class UserAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.app_name="MyApp"
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
            return
        self.balance-=amount
        print("Withdrawal successful")

def main():
    price1=100
    tax1=price1*0.1
    price2=200
    tax2=price2*0.1
    total1 = price1 + tax1
    total2=CalculateTotalPrice(price2,0.1)
    
    account=UserAccount("John Doe",1000)
    account.withdraw(200)
    
    numbers=[1,2,3,4,5]
    for i in range(len(numbers)):
        print("Number",i,":",numbers[i])
    
    if total1>total2:
        print("First total is larger")
    else:
        print("Second total is larger or equal")

    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    for row in matrix:
        for element in row:
            print(element,end=' ')
        print()

if __name__=='__main__':
    main()

