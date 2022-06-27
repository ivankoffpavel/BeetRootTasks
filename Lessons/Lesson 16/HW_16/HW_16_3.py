# Product Store
# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case
# they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to
# operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
# ```
# class Product:
#     pass
# class ProductStore:
# pass
# p = Product('Sport', 'Football T-Shirt', 100)
# p2 = Product(Food, 'Ramen, 1.5)
# s = ProductStore()
# s.add(p, 10)
# s.add(p2, 300)
# s.sell(‘Ramen’, 10)
# assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)
#
class Product:
    prod_quant = 0                # count a number of instances

    def __init__(self,type,name,price):
        self.price = price
        self.name = name
        self.type = type
        Product.prod_quant+=1
    def product_info_print(self):
        print(f'Product type {self.type},product name {self.name},product price {self.price}')
class ProductStore:
    income_amount = 0
    def __init__(self):
        self.amount = 0
        self.premium_price = 0
        self.price_rate = 1.3
        self.product_of_productstore = []

    def add(self,product,amount):
        self.premium_price = round(product.price * self.price_rate,2)
        product.price = self.premium_price
        product.amount = amount
        self.product_of_productstore.append(product)
        print(product)
    def set_discount(self,identifier, percent, identifier_type):
        self.identifier = identifier
        self.identifier_type = identifier_type
        self.percent = percent

        count = 0
        for product in self.product_of_productstore:
            product.difference = 0
            if product.name == self.identifier_type and product.type == self.identifier:
                count +=1                                                                     # special counter for circle for
                if self.percent < ((self.price_rate-1)*100):
                    product.difference = (product.price-product.price*(1-(self.percent/100))) #add new attribute and then multiple with amount
                    product.price = product.price*(1-(self.percent/100))
                    print(f'New price with discount for {product.name} is: {product.price}')
                else:
                    print('Too much percent reduce!!!')
        if count == 0:
            print('This product not exist!')


    def sell_product(self,product_name, amount):
        self.product_name = product_name
        self.amount = amount
        count = 0
        for product in self.product_of_productstore:
            count +=1                                        # special counter in order do not print else how much products in store
            if product.name == self.product_name:
                ProductStore.income_amount += product.difference*self.amount
                product.amount -= self.amount

                print(f'For name {product_name} is left {product.amount}')
        if count == 0:
            print('There is no product in store!')


    def get_all_products(self):                              # print all products in store
        count = 0
        for product in self.product_of_productstore:
            print(f'Product name: {product.name},product price: {product.price},product amount: {product.amount}, number of products:{product.prod_quant}')

    def get_product_info(self,productname):
        for product in self.product_of_productstore:
            if product.name == productname:
                return product.name,product.amount
    def get_income(self):                                     # count an income amount (saved money)
        print(f'The income is: {ProductStore.income_amount}')


p = Product('Sport','Basketball ball',25)
p1 = Product('Food','Lemon',3)
p2 = Product('Food','Apple',1.25)
# p.product_info_print()
s = ProductStore()
s.add(p,10)
s.add(p1,100)
s.add(p2,40)
s.set_discount('Food',15,'Lemon')
s.sell_product('Lemon',50)

s.get_all_products()
print(s.get_product_info('Lemon'))
s.get_income()
