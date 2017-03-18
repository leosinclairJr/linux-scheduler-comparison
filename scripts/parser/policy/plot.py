'''
XML parsing and plot benchmark for different policy

For class project 221 2017 winter

'''
#import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
from retrive_info import *

# Latt, C-Ray, 7-Zip Compression, Hackbench, FFmpeg, John The Ripper
x_name = [] # this is the names on x-axis
for name in score_dict:
    x_name.append(name)
del x_name[3] # there is a wrong name here
del x_name[1] # delete c-ray
del x_name[1] # delete 7-zip 
del x_name[2] # delete FFmpeg
N = len(x_name) # this is the number of 
print(x_name)
latt_p = [] # the policies of latt
latt_score = [] # the scores of latt
for item in score_dict['Latt']:
    latt_p.append(item[1])
    latt_score.append(int(item[2]))
#print(latt_p)
#print(latt_score)

cray_p = [] # the policies of C-Ray
cray_score = [] # the scores of C-Ray
for item in score_dict['C-Ray']:
    #print(item[2])
    cray_p.append(item[1])
    cray_score.append(float(item[2]))
#print(cray_score)
#print(latt_score)

sevenzip_p = [] # the policies of 7-zip
sevenzip_score = [] # the scores of 7-zip
for item in score_dict['7-Zip Compression']:
    #print(item)
    sevenzip_p.append(item[1])
    sevenzip_score.append(int(item[2]))
#print(sevenzip_score)

hackbench_p = [] # the policies of Hackbench
hackbench_score = [] # the scores of Hackbench
for item in score_dict['Hackbench']:
    #print(item)
    hackbench_p.append(item[1])
    hackbench_score.append(float(item[2]))
#print(hackbench_score)

ff_p = [] # the policies of FFmpeg
ff_score = [] # the scores of FFmpeg
for item in score_dict['FFmpeg']:
    #print(item)
    ff_p.append(item[1])
    ff_score.append(float(item[2]))
#print(ff_score)

jtr_p = [] # the policies of John The Ripper
jtr_score = [] # the scores of John The Ripper
for item in score_dict['John The Ripper']:
    #print(item)
    jtr_p.append(item[1])
    jtr_score.append(int(item[2]))
#print(jtr_score)

# rearrange scores
conf_list1 = []
num_config = len(latt_score)
for i in range(0,num_config):
    conf_list1.append(latt_score[i])
    conf_list1.append(hackbench_score[i])
    conf_list1.append(jtr_score[i])
#print(conf_list1)
print(num_config)
# plotting
ind = np.arange(N)  # the x locations for the groups
width = 0.15      # the width of the bars

fig, ax = plt.subplots()
#rects1 = ax.bar(left=1, 1+width, latt_score, width, color='r')
'''
p2_means = (25, 32, 34, 20, 25)
#p2_std = (3, 5, 2, 3, 3)
rects2 = ax.bar(ind, p2_means, width, color='b')

p3_means = (20, 35, 30, 35, 27)
#p1_std = (2, 3, 4, 1, 2)
rects3 = ax.bar(ind + width, p3_means, width, color='y')

p4_means = (25, 32, 34, 20, 25)
#p2_std = (3, 5, 2, 3, 3)
rects4 = ax.bar(ind + width*2, p4_means, width, color='g')

p5_means = (25, 32, 34, 20, 25)
#p2_std = (3, 5, 2, 3, 3)
rects5 = ax.bar(ind + width*2, p5_means, width, color='g')
'''
# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Benchmark')
#ax.set_xticks(ind + width / 2)
#ax.set_xticklabels(('Latt', 'C-Ray', '7-Zip', 'Hackbench', 'FFmpeg', 'John The Ripper'))
ax.set_xticklabels(x_name)
#ax.legend((rects1[0], rects2[0], rects3[0], rects4[0], rects5[0]), ('b1', 'p2', 'p3', 'p4', 'p5'))

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

#plt.show()


