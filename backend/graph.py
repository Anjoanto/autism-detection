import matplotlib.pyplot as plt
import csv


x = []
y = []

with open('free.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(int (row[0]))
        y.append(int (row[1]))

plt.plot(x, y, color='g',label="LANDMARKS")
#plt.xticks(rotation=25)
plt.xlabel('IN PIXELS')
plt.ylabel('IN PIXELS')
plt.title('AUTIWARE', fontsize=20)
plt.savefig('aut.png')
plt.grid()
plt.legend()
#plt.show()

exec(open('train.py').read())