print("think any number between 0 and 100 ")
print(" is your secret number  50 ? ")
answer = input('enter your response ')
low = 0
high = 100
mid_value = ((low+high)//2)
while (answer!='c') :
    if (answer == 'l'):
        low = mid_value 
        mid_value = (mid_value + high) // 2
    elif (answer == 'h') :
        high = mid_value
        mid_value = (mid_value + low )// 2
    else :
            print("invalid input")
    print("is your secret number ", mid_value)
    answer = input("enter your response ")
if (answer == 'c') :
     print(mid_value)