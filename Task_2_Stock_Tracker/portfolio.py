portfolio = {}
stocks = {
    "AAPL" : 180,
    "TSLA" : 250,
    "MSFT" : 370,
    "GOOG" : 450,
    "NVDA" : 480,
    "AMZN" : 175,
    "META" : 350,
    "NFLX" : 490,
    "AMD"  : 140,
    "BABA" : 75
}

while True:
    sel_stock = input("\nEnter the name of stock (Type done to stop) : ")
    if sel_stock == "DONE":
        break
    if sel_stock not in stocks:
        print("Stock is not present!!\n")
        continue  
    quan = int(input("Enter the quantity of stock: "))
    invest_val = stocks[sel_stock] * quan
    portfolio[sel_stock] = invest_val  
    invest_val_total = 0
    for ch in portfolio:
        invest_val_total += portfolio[ch]
    
print("\nPortfolio record of investment by each stock :\n", portfolio)    
print("Total investment value = ", invest_val_total)

myfile = open("portfolio.txt","w+")
myfile.write("Portfolio record of investment by each stock :\n")
myfile.write(str(portfolio) + "\n")
myfile.write(f"\nTotal investment value = {invest_val_total}\n")
myfile.close()