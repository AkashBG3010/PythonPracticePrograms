import csv        # importing CSV library

class csv():        # Parent class
    # Regular reader and writer method
    def operations_csv(start):
        if start == 1:
            with open('names.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                with open('new_names.csv', 'w') as new_file:
                    csv_writer = csv.writer(new_file, delimiter='\t')

                    for line in csv_reader:
                        csv_writer.writerow(line)

    print("Successfully read CSV file and created new CSV file to increase readability")

class main(csv):        # Subclass/ child class
    start = 1
    csv.operations_csv(start)


print("------End of program------")
