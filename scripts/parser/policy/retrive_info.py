'''
test: auto-retrive info 

'''
import os, glob, collections
import xml.etree.ElementTree as ET
#from lxml import etree
#from io import StringIO, BytesIO
# score_dict is used to store scores
score_dict = collections.defaultdict(list)

#bm_dict is used to store all data for benchmark comparesion
bm_dict = collections.defaultdict(list)

# get data from xml file 
def get_data(file):
	with open(file) as xml_data:
		tree = ET.parse(file)
		#tree_forpath = etree.parse(file)
		root = tree.getroot()
		#root_forpath = tree_forpath.getroot()
		mem_dict = collections.defaultdict(list) # memory usage
		cpu_dict = collections.defaultdict(list) # cup usage
		tem_dict = collections.defaultdict(list) # temperature
		#con_dict = collections.defaultdict(list) # config
		cnf = "" # config
		#pol_dict = collections.defaultdict(list) # policy
		#ply = ""
		#print(root.tag)
		# if Result->Identifier is not empty, then get Description as the config
		for child in root.iter('Result'):
			if child.find('Identifier').text != None and child.find('Description').text != None:
				#print(child.find('Description').text)
				cnf = child.find('Description').text
			if child.find('DisplayFormat').text == "BAR_GRAPH":
				#print(child.tag)
				for gchild in child.find('Data'):
					'''if "Communication Type" in child.find('Description').text:
						print(child.find('Description').text)
						ply = child.find('Description').text'''
						#con_dict[child.find('Description').text]
					score_dict[child.find('Title').text].append([cnf, gchild.find('Identifier').text, gchild.find('Value').text])
			elif child.find('DisplayFormat').text == "LINE_GRAPH":
				#print(child.)
				#print(child.getpath())
				#print(child.find('Arguments').text)
				if "Memory Usage" in child.find('Arguments').text:
					for gchild in child.find('Data'):
						mem_dict[child.find('Title').text].append([cnf, gchild.find('Identifier').text, [float(x) for x in gchild.find('Value').text.split(',')]])
				if "CPU Usage (Summary)" in child.find('Arguments').text:
					for gchild in child.find('Data'):
						cpu_dict[child.find('Title').text].append([cnf, gchild.find('Identifier').text, [float(x) for x in gchild.find('Value').text.split(',')]])
				if "System Temperature" in child.find('Arguments').text:
					for gchild in child.find('Data'):
						tem_dict[child.find('Title').text].append([cnf, gchild.find('Identifier').text, [float(x) for x in gchild.find('Value').text.split(',')]])
		bm_dict["memory"] = mem_dict
		bm_dict["cpu"] = cpu_dict
		bm_dict["temperature"] = tem_dict
		 			
for file in glob.glob('*.xml'):
	get_data(file)

#print(score_dict['Latt'][0][1])
#print(bm_dict['cpu']['Hackbench'])

