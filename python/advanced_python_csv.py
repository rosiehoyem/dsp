import sys
import csv


def list_of_emails(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile, skipinitialspace=True)
		emails = []
		for row in reader:
			emails.append(row['email'])
	
		fieldnames = ['email']
		writer = csv.DictWriter(open('emails.csv', 'w'), fieldnames=fieldnames)
		writer.writeheader()
		for email in emails:
			writer.writerow({'email': email})
	return writer

def main():
    arg = sys.argv[1]

    if not arg:
        print('Error: missing csv argument')
        sys.exit(1)

    list_of_emails(arg)
  
if __name__ == '__main__':
  main()