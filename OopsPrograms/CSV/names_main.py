import csv

# Regular reader and writer method
def operations_csv(start):
    if start == 1:
        with open('names.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            with open('new_names.csv', 'w') as new_file:
                csv_writer = csv.writer(new_file, delimiter='\t')

                for line in csv_reader:
                    csv_writer.writerow(line)


class main:
    start = 1
    operations_csv(start)


print("------End of program------")
