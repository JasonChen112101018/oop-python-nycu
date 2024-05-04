import matplotlib.pyplot as plt

x_vals_1 = [1, 2, 3, 4, 5, 6]
y_vals_1 = [3, 5, 6, 3, 7, 9]
plt.plot(x_vals_1, y_vals_1, 'b-', label='first')
y_vals_2 = [1, 7, 3, 5, 6, 2]
plt.plot(x_vals_1, y_vals_2, 'r--', label='second')
x_vals_2 = [1, 10, 9, 7, 3, 5]
plt.plot(x_vals_2, y_vals_2, 'g-.', label='third')
plt.plot(x_vals_2, y_vals_1, 'y:', label='fourth')
plt.plot(x_vals_2, x_vals_2, 'ko', label='fifth')
plt.legend()
plt.show()
