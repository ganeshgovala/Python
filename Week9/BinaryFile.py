with open('demo.bin', 'w') as file :
	file.write("This is a New Binary file")
	
with open('demo.bin', 'r') as file :
	print(file.read())

output :
This is a New Binary file
