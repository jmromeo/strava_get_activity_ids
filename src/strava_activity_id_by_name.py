import csv
import argparse

activity_col = 0
name_col = 2 
type_col = 3

def parse_arguments():
	parser = argparse.ArgumentParser(description='Get list of activity IDs with matching name and activity type')
	parser.add_argument('-f', '--activity_file', 
						dest='activity_file', 
						required=True, 
						type=argparse.FileType('r'),
						help="Activity csv file found in downloaded strava archive")
	parser.add_argument('-n', '--activity_name', 
						dest='activity_name', 
						required=False, 
						type=str,
						help="(Optional) Part of activity name to search")
	parser.add_argument('-t', '--activity_type', 
						dest='activity_type', 
						required=False, 
						type=str,
						help="(Optional) Type of activity to search")
	parser.add_argument('-pid', '--print_id', 
						dest='print_id', 
						required=False, 
						action='store_true',
						help="(Optional) Print only matching activity IDs and no other information")

	return parser.parse_args()

def find_matching_ids(activity_file, activity_name, activity_type):
	activity_ids = []

	with open(activity_file, newline='') as activityfile:
		activities = csv.reader(activityfile, delimiter=',')
		for row in activities:
			check_name = False if (activity_name == None) else True
			check_type = False if (activity_type == None) else True
			name_match = None if (activity_name == None) else (str.lower(activity_name) in str.lower(row[name_col]))
			type_match = None if (activity_type == None) else (str.lower(activity_type) in str.lower(row[type_col]))

			if check_name and check_type:
				if name_match and type_match:
					activity_ids.append((row[activity_col], row[name_col], row[type_col]))

			elif check_name:
				if name_match:
					activity_ids.append((row[activity_col], row[name_col], row[type_col]))

			elif check_type:
				if type_match:
					activity_ids.append((row[activity_col], row[name_col], row[type_col]))

			else:
				activity_ids.append((row[activity_col], row[name_col], row[type_col]))

	return activity_ids

args = parse_arguments()

activity_ids = find_matching_ids(args.activity_file.name, args.activity_name, args.activity_type)
for activity in activity_ids:
	if args.print_id != None:
		print(activity[0])

	else:
		print(activity)
