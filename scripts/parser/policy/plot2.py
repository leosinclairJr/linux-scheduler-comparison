'''
XML parsing script for current, cpu usage, memory usage, temperature

For class project 221 2017 winter

'''
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

'''
#tree = ET.parse('latt-test.xml')
tree = ET.parse('phoronix-results.xml')
root = tree.getroot()

# Simple data to display in various forms
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

# Four axes, returned as a 2-d array
f, axarr = plt.subplots(2, 2)
axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('current')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('CPU usage')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('memory usage')
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('default')
# Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
plt.show()
'''

test = np.array([1,2,3,4,5,6,5,4,3,5,5,])
t2 = np.array([2,2,6,4,5,6,5,4,3])

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
