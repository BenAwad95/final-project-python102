
import datetime
def persons_and_age(*args):
	people = [p.split(', ') for p in args]
	people_dict = {name: birth_date for name, birth_date in people}
	for name, birth_date in people_dict.items():
		birth_date = datetime.datetime.strptime(birth_date, '%d-%m-%Y')
		age = datetime.datetime.now() - birth_date
		people_dict[name] = age
		print(f'{name} is {age.days//365} years old and she/he was born on {birth_date.strftime("%A")}')
	old_age = max(people_dict.values())
	old_name = list(filter(lambda na: people_dict[na] == old_age, people_dict.keys()))[0]
	young_age = min(people_dict.values())
	young_name = list(filter(lambda na: people_dict[na] == young_age, people_dict.keys()))[0]
	print(f'The oldest one is {old_name}')
	print(f'The youngst one is {young_name}')





persons_and_age('Abdullah, 31-12-2018', 'khalid, 1-2-1989', 'Nouf, 2-9-2004', 'Ali, 9-12-2009')