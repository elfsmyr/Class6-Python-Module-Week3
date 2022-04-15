def computepay(hour,rate):
    
    
    if hour<=40:
        return 40*rate
    else:
        return 40*rate+(hour-40)*(rate*1.5)
        
    
hour=float(input("write hour:"))
rate=float(input("write rate:"))
print(computepay(hour,rate))

