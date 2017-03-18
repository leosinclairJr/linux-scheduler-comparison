'''
XML parsing and plot benchmark for different policy

For class project 221 2017 winter

'''
#import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
from retrive_info import *

# Latt, C-Ray, 7-Zip Compression, Hackbench, FFmpeg, John The Ripper
x_name = [] # this is the names on x-axis
for name in score_dict:
    x_name.append(name)
x_name[1] = "7-Zip"

N = len(x_name) # this is the number of 
#print(x_name)
latt_p = [] # the policies of latt
latt_score = [] # the scores of latt
for item in score_dict['Latt']:
    latt_p.append(item[1])
    latt_score.append(int(item[2]))

cray_p = [] # the policies of C-Ray
cray_score = [] # the scores of C-Ray
for item in score_dict['C-Ray']:
    #print(item[2])
    cray_p.append(item[1])
    cray_score.append(float(item[2]))

sevenzip_p = [] # the policies of 7-zip
sevenzip_score = [] # the scores of 7-zip
for item in score_dict['7-Zip Compression']:
    #print(item)
    sevenzip_p.append(item[1])
    sevenzip_score.append(int(item[2]))

# hackbench has 4 configs
hackbench_c = [] # configs of Hackbench
hackbench_p = [] # the policies of Hackbench
hackbench_score = [] # the scores of Hackbench
for i, item in enumerate(score_dict['Hackbench']):
    #print(item)
    if i%7 == 0:
        hackbench_c.append(item[0])
    hackbench_p.append(item[1])
    hackbench_score.append(float(item[2]))
#print(hackbench_c)
#print(score_dict['Hackbench'])
print(hackbench_score)
ff_p = [] # the policies of FFmpeg
ff_score = [] # the scores of FFmpeg
for item in score_dict['FFmpeg']:
    #print(item)
    ff_p.append(item[1])
    ff_score.append(float(item[2]))

#john the ripper has 3 configs
jtr_c = [] # the configs of John The Ripper
jtr_p = [] # the policies of John The Ripper
jtr_score = [] # the scores of John The Ripper
for i, item in enumerate(score_dict['John The Ripper']):
    #print(item)
    if i%7 == 0:
        jtr_c.append(item[0])
    jtr_p.append(item[1])
    jtr_score.append(int(item[2]))
#print(score_dict['John The Ripper'])
#print(jtr_c)

# modify x_name with configs
#print(x_name)
x_name[2], x_name[3] = x_name[3], x_name[2]
x_name[3] = "HB1"
x_name[4] = "JTR1"
x_name.append("HB3")
x_name.append("HB4")
x_name.append("HB2")
x_name.append("JTR2")
x_name.append("JTR3")
x_name[7], x_name[4] = x_name[4], x_name[7]
#print(x_name)

# rearrange scores
conf_list1 = []
num_config = len(latt_score)
#print(num_config)
for i in range(0,num_config):
    temp_list = []
    temp_list.append(math.log2(latt_score[i]))
    temp_list.append(math.log2(sevenzip_score[i]))
    temp_list.append(math.log2(ff_score[i]))
    temp_list.append(math.log2(hackbench_score[i]))
    temp_list.append(math.log2(jtr_score[i]))
    temp_list.append(math.log2(hackbench_score[i+14]))
    temp_list.append(math.log2(hackbench_score[i+21]))
    temp_list.append(math.log2(hackbench_score[i+7]))
    temp_list.append(math.log2(jtr_score[i+7]))
    temp_list.append(math.log2(jtr_score[i+14]))
    temp_list[4], temp_list[7] = temp_list[7], temp_list[4]
    conf_list1.append(temp_list)
print(conf_list1)
print(len(conf_list1))

# plotting
#ind = np.arange(N+5)  # the x locations for the groups
ind =  np.array([0,2,4,6,8,10,12,14,16,18])
print(ind)
width = 0.15      # the width of the bars

fig, ax = plt.subplots()
for i in range(0,num_config):
    ax.bar(ind+(i-3)*width, conf_list1[i], width,label=latt_p[i])


# add some text for labels, title and axes ticks
ax.set_ylabel('Benchmark Scores(log2)')
ax.set_title('Benchmark Tools')
ax.set_xticks(ind + width / (N+5))
#ax.set_xticklabels(('Latt', 'C-Ray', '7-Zip', 'Hackbench', 'FFmpeg', 'John The Ripper'))
ax.set_xticklabels(x_name)
#ax.legend()
ax.legend(loc='best')
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

plt.show()


