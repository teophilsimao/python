from matplotlib import pyplot as plt


x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

ax.axis([0, 5500, 0, 150_000_000_000])

ax.set_title('Cubes', fontsize=14)
ax.set_xlabel('Values', fontsize=14)
ax.set_ylabel('Cubed Values', fontsize=14)

plt.show()