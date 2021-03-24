import csv
import argparse

activity_col = 0
name_col = 2 

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

	return parser.parse_args()

args = parse_arguments()
print(args)

with open(args.activity_file.name, newline='') as activityfile:
	activities = csv.reader(activityfile, delimiter=',')
	row_num = 0
	for row in activities:
		row_num = row_num + 1
		col_num = 0
		print(f"{row[activity_col]}: {row[name_col]}")
		print(f"{row_num}")
		for col in row:
			print(f"    {col_num}: {col},")
			col_num=col_num + 1

