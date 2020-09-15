import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
mpl.rcParams['toolbar'] = 'None'
fig = plt.figure()
length = 2
points = []
points.append((0,0))


try:
    generation = int(sys.argv[1])
except:
    print("Incorrect command line arguments, format should be py toothpick.py {generation number} [line length ratio]")
    sys.exit()
try:
    line_ratio = float(sys.argv[2])
except:
    line_ratio = 1

lines = []
for i in range(generation+1):
    new_points = []
    for j in range(len(points)):
        x = points[j][0]
        y = points[j][1]
        #horizontal line
        if i%2 == 0:
            x1 = x-length/2
            y1 = y
            x2 = x + length/2
            y2 = y
        #vertical line
        else:
            x1 = x
            y1 = y - length/2
            x2 = x
            y2 = y + length/2
        plt.plot([x1,x2], [y1, y2], color = "black", linewidth=.2)
        new_points.append((x1,y1))
        new_points.append((x2,y2))
    points = new_points
    length = length * line_ratio
fig.suptitle("Gneration: " + str(generation) + " Line Ratio: " + str(line_ratio))
plt.axis('off')
plt.show()