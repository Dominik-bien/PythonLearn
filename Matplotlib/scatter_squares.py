import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Squares of numbers: ", fontsize=30)
ax.set_xlabel("Value: ", fontsize=14)
ax.tick_params(labelsize=14)

#define range for each axis
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.savefig("squares_plot.png", bbox_inches='tight')
plt.show()