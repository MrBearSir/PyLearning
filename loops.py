hrs = input("Enter Hours:")
try:
    h = float(hrs)
except:
    print("Please input your hours using numbers")
    quit()
rate = input("Enter Your Rate of Pay:")
try:
    rate = float(rate)
except:
    print("Please enter your rate using numbers ")
    quit()
if h <= 40.0:
    total = h*rate
    print(total)
else:
    h = h - 40
    total = 40*rate+rate*1.5*h
    print(total)