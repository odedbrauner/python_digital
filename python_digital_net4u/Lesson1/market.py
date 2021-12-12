tomatoPrice=3
cucamberPrice=2
colaPrice=5
ofPrice=20
print("tomato price for 1 is "+str(tomatoPrice)+" ils")
print("cucamber price for 1 is "+ str(cucamberPrice)+" ils")
print("cola price for 1 is "+ str(colaPrice)+" ils")
print("of price for 1 kilo is "+ str(ofPrice)+" ils")
tomato=int(input("how much tomatoes have you got"))
cucamber=int(input("how much cucambers have you got"))
cola=int(input("how much colas have you got"))
of=int(input("how much of have you got"))
PriceBeforeTaxes=((tomato*tomatoPrice)+(cucamber*cucamberPrice)+(cola*colaPrice)+(of*ofPrice))
print("price before taxes "+str(PriceBeforeTaxes))
price="price after taxes "+str("%.2f"%(PriceBeforeTaxes*1.17))
print(price)

