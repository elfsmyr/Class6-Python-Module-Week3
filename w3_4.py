#1
def sum_of_numbers(num1,num2):
    start=min(num1,num2)
    finish=max(num1,num2)
    
    if start==finish:
        return finish
    else:
        return start+sum_of_numbers(start+1,finish)

#2
def input_function():
    num1=int(input("write number 1:"))
    num2=int(input("write number 2:"))
    print(sum_of_numbers(num1,num2))
    
input_function()

#3
def sum_of_list(list):
    return sum(list)


print(sum_of_list([5,7,8,9]))