import matplotlib.pyplot as plt

x_values = range(0, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s=10)

# Specify a color value
#ax.scatter(x_values, y_values, color='red', s=10)

# Specify a color by (R, G, B) value
#ax.scatter(x_values, y_values, color=(0, 0.7, 0), s=10)

# Use a color gradient
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

# Save the plot to a file.
# The second agrument trims extra white space from the plot.
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()