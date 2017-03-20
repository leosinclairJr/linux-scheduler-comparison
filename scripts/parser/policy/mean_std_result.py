#mean_std_result.py
'''
This script is used to store all mean and std results into a file called mean_std_result.txt
'''

from retrive_info import *
import statistics
import math
import json
# file to store result 
#result = open('mean_std_result.txt', 'w')
#result.write("%s\n" % item)

mean_std_result = {}
for i,v in enumerate(bm_dict['cpu']):
	cpu_mean = []
	cpu_std = []
	for j,k in enumerate(bm_dict['cpu'][v]):
		cpu_mean.append(round(statistics.mean(k[2]),2))
		cpu_std.append(round(statistics.stdev(k[2]),2))
	mean_std_result[v] = {"cpu_mean":cpu_mean,"cpu_std":cpu_std, "memory_mean":None,"memory_std":None}

for i,v in enumerate(bm_dict['memory']):
	mm_mean = []
	mm_std = []
	for j,k in enumerate(bm_dict['memory'][v]):
		mm_mean.append(round(statistics.mean(k[2]),2))
		mm_std.append(round(statistics.stdev(k[2]),2))
	mean_std_result[v]["memory_mean"] = mm_mean
	mean_std_result[v]["memory_std"] = mm_std

#print(mean_std_result)
#result.write(mean_std_result)
with open('mean_std_result.json', 'w') as f:
    json.dump(mean_std_result,f)