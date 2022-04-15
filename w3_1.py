#1
def int_return():
    x=input("write integer:")
    return x
#2
def add_2():
    x=int(input("write integer:"))
    return x+2
#3
def hello():
    name=input("write yours name:")
    return "Hello {}! Nice to meet you!".format(name)
#4
def adder(*args):
    sum = 0
    for i in args:
         sum = sum + i
    return sum
#5
def list(num):
      if len(num)<5:
          print("Less than 5")
      elif len(num)>=5:
          print("Longer than 5")
#5     
def divide(num):
    return num/2

def sum(num):
    return divide(num)+6

print(sum(6))
    