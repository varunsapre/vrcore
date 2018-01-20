import re

def return_value_delete(command):
	tokens = command.split()
	#print(tokens)
	return tokens[1]
	
def return_value(command):
	tokens = command.split()
	shape_name = tokens[1]
	i = 2
	if tokens[2] not in key_words:
		shape_name += string_to_num(tokens[2])
		i += 1
	dicto = {}
	li = []
	while i < len(tokens):
		if tokens[i] in key_words:
			li_inside = []
			li_inside = [tokens[i],tokens[i+1]]
			li.append(li_inside)
			i+=2
		else:
			i+=1
	dicto[shape_name] = li
	#print(dicto)
	return dicto

def string_to_num(number):
	nums = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9',
			'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
	return nums[number]


key_words = ["length","color","coord"]


print(return_value_delete("Delete cube1")
print(return_value("Update cube one length 10 color red coord 25.5"))


#string_to_num("one")



