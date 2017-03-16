'''
test: auto-retrive info 

'''
import os, glob, collections
import xml.etree.ElementTree as ET

# score_dict is used to store scores
score_dict = collections.defaultdict(list)

#bm_dict is used to store all data for benchmark comparesion
bm_dict = collections.defaultdict(list)

# get data from xml file 
def get_data(file):
	with open(file) as xml_data:
		tree = ET.parse(file)
		root = tree.getroot()
		mem_dict = collections.defaultdict(list) # memory usage
		cpu_dict = collections.defaultdict(list) # cup usage
		tem_dict = collections.defaultdict(list) # temperature
		con_dict = collections.defaultdict(list) # config
		cnf = ""
		pol_dict = collections.defaultdict(list) # policy
		ply = ""
		#print(root.tag)
		for child in root.iter('Result'):
			if child.find('DisplayFormat').text == "BAR_GRAPH":
				#print(child.find('Title').text)
				for gchild in child.find('Data'):
					'''if "Communication Type" in child.find('Description').text:
						print(child.find('Description').text)
						con_dict[child.find('Description').text]'''
					score_dict[child.find('Title').text].append(gchild.find('Value').text)
			elif child.find('DisplayFormat').text == "LINE_GRAPH":
				#print(child.find('Arguments').text)
				if "Memory Usage" in child.find('Arguments').text:
					for gchild in child.find('Data'):
						mem_dict[child.find('Title').text].append(gchild.find('Value').text)
				if "CPU Usage (Summary)" in child.find('Arguments').text:
					for gchild in child.find('Data'):
						cpu_dict[child.find('Title').text].append(gchild.find('Value').text)
				if "System Temperature" in child.find('Arguments').text:
					for gchild in child.find('Data'):
						tem_dict[child.find('Title').text].append(gchild.find('Value').text)
		bm_dict["memory"] = mem_dict
		bm_dict["cpu"] = cpu_dict
		bm_dict["temperature"] = tem_dict
		#print(con_dict)
		 			

for file in glob.glob('*.xml'):
	get_data(file)

print(bm_dict)


