import matplotlib.pyplot as plt
from IPython import display


def plot(score, average):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title("Antrenare")
    plt.xlabel("Epoci")
    plt.ylabel("Scor")
    plt.plot(score)
    plt.plot(average)
    plt.ylim(ymin=0)
    plt.text(len(score)-1, score[-1], str(score[-1]))
    plt.text(len(average) - 1, average[-1], str(average[-1]))
    plt.show(block=False)
    plt.pause(.1)
