'''
XML parsing script for current, cpu usage, memory usage, temperature

For class project 221 2017 winter

'''
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import math
from retrive_info import *

print(bm_dict['cpu']['Latt'])
fig = plt.figure(figsize=(10, 8))

sub1 = fig.add_subplot(221) # equivalent to: plt.subplot(2, 2, 1)
sub1.set_title('current')
#for v in test:
#   sub1.plot(v)
sub1.plot(test)
sub1.plot(t2)

sub2 = plt.subplot(222)
sub2.set_title('CPU usage')
#sub2.set_xticks(())
#sub2.set_yticks(())
#sub2.text(0.5, 0.5, 'subplot(2,2,2)', ha='center', va='center', alpha=.5)
sub3 = plt.subplot(223)
sub3.set_title('memory usage')

sub4 = fig.add_subplot(224)
sub4.set_title('other')


plt.show()
