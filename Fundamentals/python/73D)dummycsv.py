
#Download a .csv file and WAP that extracts the columns indicating name, date, time, shares and price. 
#(Demonstrate your understanding of file handling, lists and dictionaries through this program).
import csv

def extract_columns(csv_file):
    extracted_data = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            date = row['Date']
            time = row['Time']
            shares = int(row['Shares'])
            price = float(row['Price'])

            extracted_data.append({
                'Name': name,
                'Date': date,
                'Time': time,
                'Shares': shares,
                'Price': price
            })

    return extracted_data

def main():
    csv_file = 'dummy.csv'
    extracted_data = extract_columns(csv_file)

    for row in extracted_data:
        print(row)

if __name__ == "__main__":
    main()

