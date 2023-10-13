symbol = input("The stock symbol:")
nshares = int(input("Number of shares:"))
bprice = float(input("The stock buying price:"))
sprice = float(input("The stock selling price:"))

total_buy_price = nshares * bprice
buy_commission = 0.03 * total_buy_price
total_sell_price = nshares * sprice
sell_commission = 0.03 * total_sell_price
profit_loss = (total_sell_price) - (total_buy_price + buy_commission + sell_commission)



print("Transactions for stock: " + symbol)
print("Bought ", nshares, "shares @ ", round(bprice, 2))
print("Paid", round(total_buy_price, 2))
print("Commission when buying: ",  round(buy_commission, 2))
print("Sold ", nshares, " shares @ ",  round(sprice, 2))
print("Received ", round(total_sell_price, 2))
print("Commission when selling: ", round(sell_commission, 2))
print("Profit or loss: ", round(profit_loss, 2))