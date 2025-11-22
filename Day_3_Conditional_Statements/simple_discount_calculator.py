amount=float(input('enter a purchase amount:'))
if amount>=2000:
    discount=amount*0.20
elif amount>=1000:
    discount=amount*0.10
else:
    discount=amount*0.05
final_price=amount-discount
print("discount ",discount)
print("final price",final_price)
