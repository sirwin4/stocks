stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak" }

purchases = [ ( 'GM', 100, '10-sep-2001', 48 ),
( 'CAT', 100, '1-apr-1999', 24 ),
( 'GM', 200, '1-jul-1998', 56 ) ]

purchase_history = []

def purchase_changes(purchases):
    for item in purchases:
        purchase_price = item[1] * item[3]
        stock_name = stockDict.get(item[0])
        purchase = (stock_name, purchase_price)
        purchase_history.append(purchase)

purchase_changes(purchases)


stocks = {}

print(type(stocks))

for item in purchases:
    if ((item[0]) in stocks):
        stocks[item[0]] = stocks[item[0]] + item[1]

    else:
        stocks.update({item[0]: item[1]})
        
    print(stocks)