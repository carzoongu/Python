import matplotlib.pyplot as pyplot

labels = ('python', 'scala', 'c#', 'java', 'PHP')
index = (1, 2, 3, 4, 5)
sizes = [45, 10, 15, 30, 22]

pyplot.bar(index(index, sizes, tick_label=labels))

pyplot.ylabel('usage')
pyplot.xlabel('Programming languages')
pyplot.show()