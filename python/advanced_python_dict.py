import sys
import csv
import operator
import itertools as it

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
'''
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}

Print the first 3 key and value pairs of the dictionary:
'''

def take(n, iterable):
    #Return first n items of the iterable as a list
    return list(it.islice(iterable, n))

def dict_sample(dictionary):
	sample = take(3, dictionary)
	dictionary_sample = {}
	for item in sample:
		dictionary_sample[item] = dictionary[item]
	return dictionary_sample

def create_lastname_dict(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile, skipinitialspace=True)
		fdict = {}
		for row in reader:
			last_name = row['name'].split()[-1]
			if last_name in fdict:
				fdict[last_name].append([row['degree'], row['title'], row['email']])
			else:
				fdict[last_name] = []
				fdict[last_name].append([row['degree'], row['title'], row['email']])
	return dict_sample(fdict)

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

'''
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }

Print the first 3 key and value pairs of the dictionary:
'''

def create_fullname_dict(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile, skipinitialspace=True)
		fdict = {}
		for row in reader:
			first_name = row['name'].split()[0]
			last_name = row['name'].split()[-1]
			name_key = (last_name, first_name)
			fdict[name_key] = []
			fdict[name_key].append(row['degree'])
			fdict[name_key].append(row['title'])
			fdict[name_key].append(row['email'])
	return dict_sample(fdict)

'''
####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value 
pairs based on alphabetical orders of the last name of the professors
'''

def create_sorted_fullname_dict(csv_file):
	with open(csv_file) as csvfile:
		reader = csv.DictReader(csvfile, skipinitialspace=True)
		fdict = {}
		for row in reader:
			first_name = row['name'].split()[0]
			last_name = row['name'].split()[-1]
			name_key = (last_name, first_name)
			fdict[name_key] = []
			fdict[name_key].append(row['degree'])
			fdict[name_key].append(row['title'])
			fdict[name_key].append(row['email'])
	for item in sorted(fdict, key=operator.itemgetter(0)):
		print(item)
		

def main():
	arg = sys.argv[1]
	if not arg:
		print('ERROR: include csv file as argument')
		sys.exit(1)
	
	print(create_lastname_dict(arg))
	print("---------------")
	print(create_fullname_dict(arg))
	print("---------------")
	create_sorted_fullname_dict(arg)
  
if __name__ == '__main__':
  main()