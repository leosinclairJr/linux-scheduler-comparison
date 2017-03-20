'''
XML parsing script for current, cpu usage, memory usage, temperature

For class project 221 2017 winter

'''
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
import statistics
from retrive_info import *

#['Latt', '7-Zip Compression', 'Hackbench', 'FFmpeg', 'John The Ripper']
# plot figsize=(10, 10)
fig = plt.figure()

colormap = plt.cm.gist_ncar
cmaps = [colormap(i) for i in np.linspace(0, 0.9, 7)]

sub1 = fig.add_subplot(121) # equivalent to: plt.subplot(2, 2, 1)
sub1.set_title('CPU usage')

sub1_policy = []
cpu_mean = []
cpu_std = []
'''
for i,v in enumerate(bm_dict['cpu']['FFmpeg']):
	sub1_policy.append(v[1])
	cpu_mean.append(round(statistics.mean(v[2]),2))
	cpu_std.append(round(statistics.stdev(v[2]),2))
	sub1.plot(v[2],color=cmaps[i],label=sub1_policy[i])
'''

# Hackbench and John The Ripper
for i in range(14,21):
	#print(bm_dict['cpu']['Hackbench'][i][2])
	sub1_policy.append(bm_dict['cpu']['John The Ripper'][i][1])
	sub1.plot(bm_dict['cpu']['John The Ripper'][i][2],color=cmaps[i-14],label=sub1_policy[i-14])


sub2 = plt.subplot(122)
sub2.set_title('memory usage')

sub2_policy = []
mm_mean = []
mm_std = []
plt2 = []

# Hackbench and John The Ripper
for i in range(14,21):
	#print(bm_dict['cpu']['Hackbench'][i][2])
	sub2_policy.append(bm_dict['memory']['John The Ripper'][i][1])
	plotobj = sub2.plot(bm_dict['memory']['John The Ripper'][i][2],color=cmaps[i-14],label=sub2_policy[i-14])
	plt2.append(plotobj[0])
'''
for i,v in enumerate(bm_dict['memory']['FFmpeg']):
	sub2_policy.append(v[1])
	mm_mean.append(round(statistics.mean(v[2]),2))
	mm_std.append(round(statistics.stdev(v[2]),2))
	plotobj = sub2.plot(v[2],color=cmaps[i],label=sub2_policy[i])
	plt2.append(plotobj[0])
'''
#sub1.set_xticklabels(sub1_policy,size='x-small',stretch='extra-condensed', rotation=20, ha='right')
sub2.legend(bbox_to_anchor=(1, 1.02))

'''
# create a legend label array 
label_arr = []
for i in range(0,7):
	label_arr.append('('+str(cpu_mean[i])+","+str(cpu_std[i])+')('+str(mm_mean[i])+","+str(mm_std[i])+')')

fig.legend(loc='best',handles=plt2,labels=label_arr)
'''
plt.show()
