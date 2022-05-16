#Continuously updates the average as new numbers are entered.
num_data=1
num2=0
sum=0
while True:
    num1 = input("Input the data ")
    try:
        num2=int(num1)
    except ValueError:
        print("You input incorrect information ")
    else:
        sum+=num2
        average=sum/num_data
        print(f"Average is {average}")
        num_data+=1