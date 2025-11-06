import matplotlib.pyplot as plt
import numpy as np


data = np.random.randn(1000)





plt.hist(data, bins=20, color='green')
plt.title("Histogram")

plt.tight_layout()
plt.show()

