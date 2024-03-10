import numpy as np
import matplotlib.pyplot as plt
x = np.array([1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0])
def T(n):
	if n==0:
		return 0.9*1
	else:
		return 0.8*T(n-1) + 0.18*x[n]
y_values = np.zeros((16,))
for i in range(x.shape[0]):
	y_values[i] = T(i)
print(y_values)

plt.figure(figsize=(10, 5))
plt.stem(range(16), y_values, use_line_collection=True)
plt.title('Plot of y(n) vs. n')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()