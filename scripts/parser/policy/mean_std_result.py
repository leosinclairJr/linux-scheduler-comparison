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
#['Latt', '7-Zip Compression', 'Hackbench', 'FFmpeg', 'John The Ripper']

mean_std_result = {}
for i,v in enumerate(bm_dict['cpu']):
	cpu_mean = []
	cpu_std = []
	if v == 'Hackbench': 
		con_mean1,con_mean2,con_mean3,con_mean4 = [],[],[],[]
		con_std1,con_std2,con_std3,con_std4 = [],[],[],[]
		for n in range(0,7):
			con_mean1.append(round(statistics.mean(bm_dict['cpu'][v][n][2]),2))
			con_std1.append(round(statistics.stdev(bm_dict['cpu'][v][n][2]),2))
		for n in range(7,14):
			con_mean2.append(round(statistics.mean(bm_dict['cpu'][v][n][2]),2))
			con_std2.append(round(statistics.stdev(bm_dict['cpu'][v][n][2]),2))
		for n in range(14,21):
			con_mean3.append(round(statistics.mean(bm_dict['cpu'][v][n][2]),2))
			con_std3.append(round(statistics.stdev(bm_dict['cpu'][v][n][2]),2))
		for n in range(21,28):
			con_mean4.append(round(statistics.mean(bm_dict['cpu'][v][n][2]),2))	
			con_std4.append(round(statistics.stdev(bm_dict['cpu'][v][n][2]),2))		
		cpu_mean = [con_mean1,con_mean2,con_mean3,con_mean4]
		cpu_std = [con_std1,con_std2,con_std3,con_std4]
		#print(cpu_mean)
	elif v == 'John The Ripper':
		con_jtr_mean1,con_jtr_mean2,con_jtr_mean3 = [],[],[]
		con_jtr_std1,con_jtr_std2,con_jtr_std3 = [],[],[]
		for n in range(0,7):
			con_jtr_mean1.append(round(statistics.mean(bm_dict['cpu'][v][n][2]),2))
			con_jtr_std1.append(round(statistics.stdev(bm_dict['cpu'][v][n][2]),2))
		for n in range(7,14):
			con_jtr_mean2.append(round(statistics.mean(bm_dict['cpu'][v][n][2]),2))
			con_jtr_std2.append(round(statistics.stdev(bm_dict['cpu'][v][n][2]),2))
		for n in range(14,21):
			con_jtr_mean3.append(round(statistics.mean(bm_dict['cpu'][v][n][2]),2))
			con_jtr_std3.append(round(statistics.stdev(bm_dict['cpu'][v][n][2]),2))
		cpu_mean = [con_jtr_mean1,con_jtr_mean2,con_jtr_mean3]
		cpu_std = [con_jtr_std1,con_jtr_std2,con_jtr_std3]
	else:
		for j,k in enumerate(bm_dict['cpu'][v]):
			cpu_mean.append(round(statistics.mean(k[2]),2))
			cpu_std.append(round(statistics.stdev(k[2]),2))
	mean_std_result[v] = {"cpu_mean":cpu_mean,"cpu_std":cpu_std, "memory_mean":None,"memory_std":None}
#print(mean_std_result)
for i,v in enumerate(bm_dict['memory']):
	mm_mean = []
	mm_std = []
	if v == 'Hackbench': 
		con_mean1,con_mean2,con_mean3,con_mean4 = [],[],[],[]
		con_std1,con_std2,con_std3,con_std4 = [],[],[],[]
		for n in range(0,7):
			con_mean1.append(round(statistics.mean(bm_dict['memory'][v][n][2]),2))
			con_std1.append(round(statistics.stdev(bm_dict['memory'][v][n][2]),2))
		for n in range(7,14):
			con_mean2.append(round(statistics.mean(bm_dict['memory'][v][n][2]),2))
			con_std2.append(round(statistics.stdev(bm_dict['memory'][v][n][2]),2))
		for n in range(14,21):
			con_mean3.append(round(statistics.mean(bm_dict['memory'][v][n][2]),2))
			con_std3.append(round(statistics.stdev(bm_dict['memory'][v][n][2]),2))
		for n in range(21,28):
			con_mean4.append(round(statistics.mean(bm_dict['memory'][v][n][2]),2))	
			con_std4.append(round(statistics.stdev(bm_dict['memory'][v][n][2]),2))		
		mm_mean = [con_mean1,con_mean2,con_mean3,con_mean4]
		mm_std = [con_std1,con_std2,con_std3,con_std4]
		#print(cpu_mean)
	elif v == 'John The Ripper':
		con_jtr_mean1,con_jtr_mean2,con_jtr_mean3 = [],[],[]
		con_jtr_std1,con_jtr_std2,con_jtr_std3 = [],[],[]
		for n in range(0,7):
			con_jtr_mean1.append(round(statistics.mean(bm_dict['memory'][v][n][2]),2))
			con_jtr_std1.append(round(statistics.stdev(bm_dict['memory'][v][n][2]),2))
		for n in range(7,14):
			con_jtr_mean2.append(round(statistics.mean(bm_dict['memory'][v][n][2]),2))
			con_jtr_std2.append(round(statistics.stdev(bm_dict['memory'][v][n][2]),2))
		for n in range(14,21):
			con_jtr_mean3.append(round(statistics.mean(bm_dict['memory'][v][n][2]),2))
			con_jtr_std3.append(round(statistics.stdev(bm_dict['memory'][v][n][2]),2))
		mm_mean = [con_jtr_mean1,con_jtr_mean2,con_jtr_mean3]
		mm_std = [con_jtr_std1,con_jtr_std2,con_jtr_std3]
	else:
		for j,k in enumerate(bm_dict['memory'][v]):
			mm_mean.append(round(statistics.mean(k[2]),2))
			mm_std.append(round(statistics.stdev(k[2]),2))
	mean_std_result[v]["memory_mean"] = mm_mean
	mean_std_result[v]["memory_std"] = mm_std

#print(mean_std_result)
#result.write(mean_std_result)
with open('mean_std_result.json', 'w') as f:
    json.dump(mean_std_result,f)


