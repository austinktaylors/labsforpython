itemprice = float(input('Enter item price: '))
salestax = float(input('Enter sales tax percent: '))
taxtopercent = salestax * .01
costofitem = print(f'The item price is ${taxtopercent * itemprice + itemprice:.2f}')