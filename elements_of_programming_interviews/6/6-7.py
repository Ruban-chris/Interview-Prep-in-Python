# Write a program that takes an array denoting the daily stock price, and returns
# the maximum profit that could be made by buying and then selling one share of 
# that stock

myStockPrices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

# def makeMostMoney(stockPrices):
#     if len(stockPrices) is 0: return 0
#     
#     shareBoughtPointer = 0
#     maximumProfit = -1
#     
#     while shareBoughtPointer < len(stockPrices):
#         for i in range(shareBoughtPointer + 1, len(stockPrices)):
#             profit = stockPrices[i] - stockPrices[shareBoughtPointer]
#             if maximumProfit < profit:
#                 print('stockPrices[shareBoughtPointer]', stockPrices[shareBoughtPointer])
#                 print('stockPrices[i]', stockPrices[i])
#                 maximumProfit = profit
#         shareBoughtPointer += 1
#     
#     return maximumProfit
# 
# print(makeMostMoney(myStockPrices))

def computeMaxProfit(prices):
    minPrice = 999999999999
    maxPrice = 0
    maxProfit = 0
    for price in prices:
        maxProfit = max(maxProfit, price - minPrice)
        minPrice = min(minPrice, price)
    return maxProfit
    
print(computeMaxProfit(myStockPrices))