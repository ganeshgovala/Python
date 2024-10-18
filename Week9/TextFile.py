with open('demo.txt', 'w') as file :
	file.write("This is a new file")
	
with open('demo.txt', 'r') as file :
	print(file.read())

output :
This is a new file
