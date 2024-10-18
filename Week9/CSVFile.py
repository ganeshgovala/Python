import csv

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

with open('CSV.csv', 'w', newline='') as file :
	writer = csv.writer(file)
	writer.writerows(data)
	
with open('CSV.csv', 'r') as file :
	reader = csv.reader(file)
	for i in reader :
		print(i)

output :
['Name', 'Age', 'City'],
['Alice', 30, 'New York'],
['Bob', 25, 'Los Angeles'],
['Charlie', 35, 'Chicago'] 
