file_path = "data.txt"

parsed_data_C1 = []
parsed_data_C2 = []

# Open and read the file
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split()
        parsed_data_C1.append(int(parts[0]))
        parsed_data_C2.append(int(parts[1]))

parsed_data_C1.sort();
parsed_data_C2.sort();
i = 0
FinalSum = 0

for item in parsed_data_C1:
    FinalSum += abs(parsed_data_C1[i] - parsed_data_C2[i])
    i += 1

print(FinalSum)

FinalProduct = 0
j = 0

for item in parsed_data_C1:
    counter = 0
    for freq in parsed_data_C2:
        if item == freq:
            counter += 1
    FinalProduct += item*counter

print(FinalProduct)

