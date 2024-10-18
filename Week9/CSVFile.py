with open('demo.csv', 'w') as file :
	file.write("This is a New CSV file")
	
with open('demo.csv', 'r') as file :
	print(file.read())

output :
This is a New CSV file
