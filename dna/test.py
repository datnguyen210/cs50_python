import csv

csv_file_path = 'databases/small.csv'

data_list = []

with open(csv_file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        for key in row:
            if key != 'name':  # Skip the 'name' field
                row[key] = int(row[key])
        data_list.append(row)

print(data_list)
