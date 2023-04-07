import csv
import nltk

with open('tois.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
    next(reader)
   
    output_rows = []

    for row in reader:
        TIC = row[2]
        FULL_TOI_ID = row[3]

        print('Description:', TIC)
        output_rows.append([TIC, FULL_TOI_ID])

with open('TOILOOKOUTS.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['Data Contents'])
    writer.writerow(['TIC, FULL_TOI_ID'])

    for row in output_rows:
        writer.writerow(row)