# import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    pointers_numbers = range(rw.num_points)
    #ax.scatter(rw.x_values, rw.y_values, c=pointers_numbers, cmap=plt.cm.Reds,
    #           edgecolors='none', s=1)
    ax.plot(rw.x_values, rw.y_values, lw=1)
    ax.set_aspect('equal')
    
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)
    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    user_input = input('More? (y/n): ')
    if user_input.lower() == 'n':
        break 



