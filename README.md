# SWE_Onymos - Stock Trading Engine

## 🚀 Overview
This project is a **lock-free, real-time stock trading engine** designed to match buy and sell orders for up to **1,024 unique tickers** without using built-in dictionaries or external libraries.
## 🛠️ Design Explanation
### ✅ How Orders Are Stored
To manage up to **1,024 different stock tickers**, the system uses an array of size **1,024** to store Buy and Sell orders.  
When a new order is received, its index in the array is calculated using the ticker symbol:
            index = sum(ord(character) * (10 ** position)) % 1024
- This formula converts the characters of the stock's ticker symbol into a numerical value.
- Using this method ensures that each ticker symbol gets mapped to a specific slot in the array.
- Since different companies can have the **same ticker symbol**, this index calculation helps distribute and organize the orders across the array.
- This allows fast access and avoids the use of built-in data structures like dictionaries.

### ✅ How I Avoid Multithreading Issues Without Locks
This system is designed to handle multiple threads conceptually **without using any threading libraries or locks**.

The key idea is that **each order is assigned a unique `ID`** when created.  
This `ID` ensures that:
- Even if two threads try to delete the same Buy and Sell orders at the same time, only **one thread can successfully delete an order by its ID**.
- If one thread removes an order, the second thread **cannot remove the same order again**, because the order no longer exists in the list.
- This prevents duplicate deletions or corruption of the order book without using locks.

### ✅ Why this works:
| 🛠️ Problem | 💡 Solution |
|------------|-------------|
| Same ticker symbols across companies | Calculate a unique index based on the ticker's characters. |
| Multiple threads modifying the order book | Assign unique IDs to each order and check IDs before deletion. |
| No locks or thread safety tools allowed | Unique IDs act as a soft protection against duplicate operations. |

---
### ✅ Summary:
- ✅ Supports **1,024 ticker symbols** with custom indexing.
- ✅ Avoids race conditions and double deletions using **unique IDs**.
- ✅ Does **not** use dictionaries, maps, or any external libraries.
- ✅ Fully lock-free, based on careful data design with linked lists and IDs.
