#test cases
from SWE_Onymos import stock, Trading

# ✅ Test 1: Start with just one stock
print("\n✅ Test 1: Single stock")
root = stock("AAPL", 100, 150.0)
print(root)

# ✅ Test 2: Add stocks with decreasing prices (they go to the end)
print("\n✅ Test 2: Add stocks with lower prices")
root.add_node(50, 100.0)
root.add_node(75, 80.0)
print(root)

# ✅ Test 3: Add a stock that belongs in the middle
print("\n✅ Test 3: Add stock between AAPL and TSLA")
root.add_node(200, 120.0)
print(root)

# ✅ Test 4: Add a stock with the highest price (becomes new root)
print("\n✅ Test 4: Add stock with highest price")
root.add_node(300, 200.0)
print(root)

# ✅ Test 5: Add a stock with the lowest price (goes at the end)
print("\n✅ Test 5: Add stock with lowest price")
root.add_node(60, 50.0)
print(root)

# Extra tests
print("\n✅ Test 6: Add duplicate price")
root.add_node(120, 150.0)
print(root)

print("\n✅ Test 7: Add mid-range price")
root.add_node(80, 90.0)
print(root)

print("\n✅ Test 8: Final list check")
print(root)

#---------------------------------
# ✅ Initialize the trading system
trade = Trading()

# ✅ Test 1: Add Buy Orders
print("\n✅ Test 1: Add Buy Orders")
trade.addOrder("Buy", "AAPL", 100, 150)
trade.addOrder("Buy", "AAPL", 50, 140)
trade.addOrder("Buy", "AAPL", 30, 130)
print(trade)

# ✅ Test 2: Add Sell Orders
print("\n✅ Test 2: Add Sell Orders")
trade.addOrder("Sell", "AAPL", 80, 120)
trade.addOrder("Sell", "AAPL", 60, 125)
trade.addOrder("Sell", "AAPL", 40, 135)
print(trade)

# ✅ Test 3: Match Orders (should match some orders)
print("\n✅ Test 3: Match Orders")
trade.matchOrder()
print(trade)

# ✅ Test 4: No Match Available (buy price < sell price)
print("\n✅ Test 4: No Match Available")
trade.addOrder("Buy", "TSLA", 50, 100)
trade.addOrder("Sell", "TSLA", 60, 200)
print(trade)
trade.matchOrder()
print(trade)

# ✅ Test 5: Partial Match (quantities don't fully match)
print("\n✅ Test 5: Partial Match")
trade.addOrder("Buy", "GOOG", 100, 300)
trade.addOrder("Sell", "GOOG", 50, 250)
print(trade)
trade.matchOrder()
print(trade)

# ✅ Test 6: Exact Match (same quantity and price)
print("\n✅ Test 6: Exact Match")
trade.addOrder("Buy", "META", 100, 180)
trade.addOrder("Sell", "META", 100, 180)
print(trade)
trade.matchOrder()
print(trade)

# ✅ Test 7: Multiple Symbols Active
print("\n✅ Test 7: Multiple Symbols Active")
trade.addOrder("Buy", "NFLX", 150, 160)
trade.addOrder("Sell", "NFLX", 150, 150)
trade.addOrder("Buy", "AMZN", 200, 300)
trade.addOrder("Sell", "AMZN", 100, 280)
print(trade)
trade.matchOrder()
print(trade)