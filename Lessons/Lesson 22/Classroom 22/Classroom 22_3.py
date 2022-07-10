# Create a Taxable Income Calculator, where inputs are income and % of tax.
def income_calc(a:float,tax:int)->float:
    return a*(tax/100)
print(income_calc(200,30))