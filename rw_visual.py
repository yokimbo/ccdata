import matplotlib.pyplot as plt

from random_walk import RandomWalk

keep_running = 'y'

while keep_running == 'y':

    # Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    # Set the aspect of the axes. 1 = 'equal'.
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_aspect.html 
    ax.set_aspect(1)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")