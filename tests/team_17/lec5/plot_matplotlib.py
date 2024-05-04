import matplotlib.pyplot as plt

# x coordinates
x_vals_1 = [1, 2, 3, 4, 5, 6]
x_vals_2 = [3, 5, 6, 3, 7, 9]
x_vals_3 = [3, 4, 5, 6, 7, 8]

# y coordinates
y_vals_1 = [1, 7, 3, 5, 6, 2]
y_vals_2 = [1, 10, 9, 7, 3, 5]

# plot
plt.plot(x_vals_1, y_vals_1, 'b-', label='first')
plt.plot(x_vals_1, y_vals_2, 'r--', label='second')
plt.plot(x_vals_2, y_vals_1, 'g-.', label='third')
plt.plot(x_vals_2, y_vals_2, 'y:', label='fourth')
plt.plot(x_vals_3, y_vals_1, 'k', label='fifth')
plt.plot(x_vals_3, y_vals_2, 'm+', label='sixth')

# labels
plt.legend()
plt.show()
