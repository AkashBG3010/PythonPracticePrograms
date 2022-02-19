import csv


# Regular reader and writer method
def operations_csv():

    with open('contact.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        with open('new_contact.csv', 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter='\t')

            for line in csv_reader:
                csv_writer.writerow(line)


class main:
    operations_csv()

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
