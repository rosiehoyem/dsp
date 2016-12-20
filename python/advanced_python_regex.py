import sys
import csv
import re

###Part I - Regular Expressions  

####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

def not_a_null_value(degree):
	if degree is not '0':
		return True
	else:
		return False

def degree_frequency(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile, skipinitialspace=True)
		frequencies = {}
		for row in reader:
			degrees = row['degree'].split()
			for degree in degrees:
				degree = degree.replace('.', '')
				if degree in frequencies:
					frequencies[degree] = frequencies[degree] + 1
				elif not_a_null_value(degree):
					frequencies[degree] = 1
				else:
					None
	return frequencies

def title_frequency(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile, skipinitialspace=True)
		frequencies = {}
		for row in reader:
			title = row['title']
			if title in frequencies:
				frequencies[title] = frequencies[title] + 1
			else:
				frequencies[title] = 1
	return frequencies

def list_of_emails(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile, skipinitialspace=True)
		emails = []
		for row in reader:
			emails.append(row['email'])
	return emails

def email_domain_frequency(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile, skipinitialspace=True)
		frequencies = {}
		for row in reader:
			email = row['email']
			match = re.search('([\w.-]+)@([\w.-]+)',email)
			domain = match.group(2)
			if domain in frequencies:
				frequencies[domain] = frequencies[domain] + 1
			else:
				frequencies[domain] = 1
	return frequencies

def number_of_items(frequencies):
	return len(frequencies)

def main():
	arg = sys.argv[1]
	if not arg:
		print('ERROR: include csv file as argument')
		sys.exit(1)
	
	####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.
	print(number_of_items(degree_frequency(arg)))
	print(degree_frequency(arg))

	####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor
	print(number_of_items(title_frequency(arg)))
	print(title_frequency(arg))
	
	####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.
	print(list_of_emails(arg))
	
	####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.
	print(number_of_items(email_domain_frequency(arg)))
	print(email_domain_frequency(arg))
	
  
if __name__ == '__main__':
  main()