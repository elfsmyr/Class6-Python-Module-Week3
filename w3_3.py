#1
pi=3.14

#2

def sphere_area(r):
    return pi*r**2
#3
def sphere_volume(r):
    volume=4/3*sphere_area(r)*r
    return volume

def sphere(r):
    return sphere_area(r),sphere_volume(r)
    
print("area: {} volume:{} ".format(sphere(3)[0],sphere(3)[1]))