import pickle
import glob
from cmd_token import *

def process(cmd,coord,pathVar):
	store = {}
	if len(glob.glob("*.pkl")) != 0:
		with open('data.pkl', 'rb') as pickle_file:
			store = pickle.load(pickle_file)
		pickle_file.close()

	#cmd = "Insert cube one color red"
	#cmd = "Insert sphere one color red radius 20"
	#cmd = "Insert cylinder two"
	#cmd = "Delete sphere one"

	if cmd.split()[0].lower() == "insert":
		dicto = return_value(cmd)
		shape = list(dicto.keys())[0]

		if "cube" in shape:
			cr = 'color = "black"'
			if dicto[shape]["color"] != None:
				cr = ' color = "' + dicto[shape]["color"] + '" '
			liner = '<a-box position="'+' '.join(map(str,coord))+'" rotation="0 45 0"'+ cr +'shadow="" material="" geometry=""></a-box>'
			#print(liner)

		if "sphere" in shape:
			cr = 'color = "black"'
			r = 'radius = "1.25"'
			if dicto[shape]["color"] != None:
				cr = ' color = "' + dicto[shape]["color"] + '" '
			if dicto[shape]["radius"] != None:
				r = ' radius = "' + dicto[shape]["radius"] + '" '
			liner = '<a-sphere position="'+' '.join(map(str,coord))+'"' + cr + r + 'shadow="" material="" geometry=""></a-sphere>'
			#print(liner)

		if "cylinder" in shape:
			cr = 'color = "black"'
			r = 'radius = "0.5"'
			h = 'height = "1.5"'
			if dicto[shape]["color"] != None:
				cr = ' color = "' + dicto[shape]["color"] + '" '
			if dicto[shape]["radius"] != None:
				r = ' radius = "' + dicto[shape]["radius"] + '" '
			if dicto[shape]["height"] != None:
				h = ' height = "' + dicto[shape]["height"] + '" '
			liner = '<a-cylinder position="'+' '.join(map(str,coord))+'"' + cr+r+h +'shadow="" material="" geometry=""></a-cylinder>'
			#print(liner)
		store[shape] = liner

	output = open('data.pkl', 'wb')
	pickle.dump(store, output)
	output.close()

	if cmd.split()[0].lower() == "update":
		print(return_value(cmd))


	if cmd.split()[0].lower() == "delete":
		shape_name = return_value_delete(cmd)
		with open('data.pkl', 'rb') as pickle_file:
			store = pickle.load(pickle_file)
		pickle_file.close()

		del store[shape_name]

		output = open('data.pkl', 'wb')
		pickle.dump(store, output)
		output.close()

	string = ''
	for keys in store:
		string += store[keys]
		string += "\n"
		#print(keys)
	#print(string)

	header = '<canvas class="a-canvas" data-aframe-canvas="true" width="300" height="150"></canvas><a-camera universal-controls wasd-controls><a-cursor></a-cursor></a-camera>'
	footer = '<a-sky src = "' + pathVar + '" ></a-sky>'

	body = header + string + footer
	#print(body)
	return body


#process("Insert cube three color red",[1,1,1],"1.jpg")
