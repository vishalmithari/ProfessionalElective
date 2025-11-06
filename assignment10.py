import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 25, 30, 35]
y1 = [10, 20, 25, 30, 35]
y2 = [15, 18, 22, 27, 33]
sizes = [30, 25, 20, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']

plt.figure(figsize=(10,6))


plt.subplot(2,2,2)
plt.bar(x, y2, color='orange')
plt.title("Bar Chart")

plt.subplot(2,2,3)
plt.plot(x, y)                           
plt.fill_between(x, y, 0, alpha=0.3)    
plt.title("Monthly Sales – Area Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()



plt.tight_layout()
plt.show()

