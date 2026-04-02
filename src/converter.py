import csv
import datetime

def convert_date(date_string):
    try:
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return date_string
    except:
        date_object = datetime.datetime.strptime(date_string, "%B %d, %Y")
        converted = date_object.strftime("%Y-%m-%d")
        return converted

def process_file(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if not row:
                writer.writerow(row)
                continue
            else:
                converted = convert_date(", ".join(row))
                writer.writerow([converted])