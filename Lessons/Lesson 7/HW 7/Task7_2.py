# Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.
stock = {"banana": 6,"apple": 0,"orange": 32,"pear": 15}
prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
def sum_of_stok(a,b):
    res = [value1*value for key,value in stock.items() for key1,value1 in prices.items() if key == key1]
    sum = 0
    for i in res:
        sum += i
    print(f'The sum of goods is: {sum}')
sum_of_stok(stock,prices)
