import matplotlib.pyplot as plt

from random_walk import RandomWalk

keep_running = 'y'

while keep_running == 'y':

    # Make a random walk.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10,6), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    # Set the aspect of the axes. 1 = 'equal'.
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html 
    ax.set_aspect(1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)


    plt.show()

    # keep_running = input("Make another walk? (y/n): ")
    keep_running = 'n'