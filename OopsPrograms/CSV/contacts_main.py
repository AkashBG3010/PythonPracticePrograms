import csv        # importing CSV library


class csv_file_operation():        # Parent class
    # Regular reader and writer method
    def operation(self):
        if start == 1:
            with open('contact.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)

                with open('new_contact.csv', 'w') as new_file:
                    csv_writer = csv.writer(new_file, delimiter='\t')

                    for line in csv_reader:
                        csv_writer.writerow(line)
        print("Successfully read CSV file and created new CSV file to increase readability")


class main(csv_file_operation):        # Subclass/ child class
    if __name__ == '__main__':
        start = 1
        csv_file_operation.operation(start)


print("------End of program------")



# Dictionary reader and writer method
#
# with open('contact.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('new_contact.csv', 'w') as new_file:
#         fieldnames = ['ICON_GID', 'ICON_XID', 'DESCRIPTION', 'PATH']
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')
#         fieldnames.writeheader()
#
#         for line in csv_reader:
#             del line['DOMAIN_NAME']
#             csv_writer.writerow(line)
