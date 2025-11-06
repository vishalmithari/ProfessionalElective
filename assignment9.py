import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [20000, 25000, 22000, 27000, 30000]
profit = [4000, 5000, 3500, 6000, 7000]

plt.subplot(1, 2, 1)
plt.bar(months, sales, color='lightblue', label='Sales')
plt.plot(months, profit, color='red', marker='o', label='Profit')
plt.title("Sales and Profit Comparison")
plt.xlabel("Months")
plt.ylabel("Amount (₹)")
plt.legend()

plt.subplot(1, 2, 2)
plt.pie(sales, labels=months, autopct='%1.1f%%')
plt.title("Sales Distribution")

plt.tight_layout()
plt.show()
