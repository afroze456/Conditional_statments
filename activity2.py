accual_cost= float(input("enter the accual cost "))
sale_cost=float(input("enter the sale cost "))

if sale_cost>accual_cost:
    profit=sale_cost-accual_cost
    print("you have a profit of", profit)

else:
    print("the was no profit")