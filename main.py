
import datetime
def persons_and_age(*args):
	people = [p.split(', ') for p in args]
	people_dict = {name: birth_date for name, birth_date in people}
	for name, birth_date in people_dict.items():
		try:
			birth_date = datetime.datetime.strptime(birth_date, '%d-%m-%Y')
			age = datetime.datetime(2021,1,1) - birth_date
			people_dict[name] = age
			print(f'{name} is {age.days//365} years old and she/he was born on {birth_date.strftime("%A")}')
		except ValueError:
			print(f'{name} has Invalid date')
			return None
	old_age = max(people_dict.values())
	old_name = list(filter(lambda na: people_dict[na] == old_age, people_dict.keys()))[0]
	young_age = min(people_dict.values())
	young_name = list(filter(lambda na: people_dict[na] == young_age, people_dict.keys()))[0]
	if len(people_dict) > 1:
		print(f'The oldest one is {old_name}')
		print(f'The youngst one is {young_name}')
		print(f'Total People: {len(people_dict)}')
	else:
		print('There is no oldest or youngest person')





persons_and_age('Abdullah, 31-12-1995')