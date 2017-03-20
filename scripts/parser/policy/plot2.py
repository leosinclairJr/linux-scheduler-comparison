'''
XML parsing script for current, cpu usage, memory usage, temperature

For class project 221 2017 winter

'''
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
from retrive_info import *

# there are 7 configs, bm_dict['cpu']['Latt'][0], bm_dict['cpu']['Latt'][1]...
#print(bm_dict['cpu']['Latt'][0])
# the values(list) of each config bm_dict['cpu']['Latt'][0][2]
#print(bm_dict['cpu']['Latt'][0][2])
# convert the string to int

#figsize=(20, 10)
fig = plt.figure()

colormap = plt.cm.gist_ncar
cmaps = [colormap(i) for i in np.linspace(0, 0.9, 7)]

sub1 = fig.add_subplot(121) # equivalent to: plt.subplot(2, 2, 1)
sub1.set_title('CPU usage')

sub1_policy = []
for i,v in enumerate(bm_dict['cpu']['Latt']):
	sub1_policy.append(v[1])
	sub1.plot(v[2],color=cmaps[i],label=sub1_policy[i])
#sub1.set_xticklabels(sub1_policy,size='x-small',stretch='extra-condensed', rotation=20, ha='right')
sub1.legend()


sub2 = plt.subplot(122)
sub2.set_title('memory usage')

sub2_policy = []
for i,v in enumerate(bm_dict['memory']['Latt']):
	sub2_policy.append(v[1])
	sub2.plot(v[2],color=cmaps[i],label=sub2_policy[i])
#sub1.set_xticklabels(sub1_policy,size='x-small',stretch='extra-condensed', rotation=20, ha='right')
sub2.legend()


plt.show()
