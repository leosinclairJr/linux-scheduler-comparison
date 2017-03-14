'''
XML parsing and plot benchmark for different policy

For class project 221 2017 winter

'''
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np


#tree = ET.parse('latt-test.xml')
tree = ET.parse('phoronix-results.xml')
root = tree.getroot()

# this list used to store score for different policy
pl = (int(root[25][8][0][1].text),int(root[25][8][1][1].text),int(root[25][8][2][1].text),int(root[25][8][3][1].text),int(root[25][8][4][1].text))

#for child in root.iter('Result'):
	#print(child.tag, child.attrib, child.find('Identifier').text)
	#print(len(child))
	#print(child[8][0].find('Identifier').text, child[8][0].find('Value').text)
	#arr.append(child[8][0].find('Value').text, child[8][1].find('Value').text, child[8][2].find('Value').text) 
print(root[25][8][4][1].text)

N = 5
p1_means = pl#(20, 35, 30, 35, 27)
#p1_std = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.15      # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width, p1_means, width, color='r')

p2_means = pl#(25, 32, 34, 20, 25)
#p2_std = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind, p2_means, width, color='b')

p3_means = pl#(20, 35, 30, 35, 27)
#p1_std = (2, 3, 4, 1, 2)
rects3 = ax.bar(ind + width, p3_means, width, color='y')

p4_means = pl#(25, 32, 34, 20, 25)
#p2_std = (3, 5, 2, 3, 3)
rects4 = ax.bar(ind + width*2, p4_means, width, color='g')

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Benchmark')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('b1', 'b2', 'b3', 'b4', 'b5'))

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('p1', 'p2', 'p3', 'p4'))

'''
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
'''

plt.show()