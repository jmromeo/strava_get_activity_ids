import shutil
import argparse
import gzip
import subprocess

def parse_arguments():
	parser = argparse.ArgumentParser(description='Merge fit files')
	parser.add_argument('-f', '--fit_file_list', 
						dest='fit_file_list', 
						required=True, 
						type=argparse.FileType('r'),
						help="List of fit files to merge")
	parser.add_argument('-b', '--base_directory', 
						dest='base_directory', 
						required=True, 
						type=str,
						help="Downloaded activity archive directory")
	parser.add_argument('-d', '--output_directory', 
						dest='output_directory', 
						required=True, 
						type=argparse.FileType('w'),
						help="Directory to output gpx files")

	return parser.parse_args()

def unzip_file(file):
	unzipped_file = ""

	with gzip.open(file, 'rb') as zipped_file:
		with open(file[0:-3], 'wb') as unzipped_file:
			shutil.copyfileobj(zipped_file, unzipped_file)

	return unzipped_file.name

def convert_fit_to_gpx(fitfile):
	gpsbabel_cmd = f"gpsbabel -i garmin_fit -f {fitfile} -o gpx -F {fitfile[0:-4]}.gpx"
	subprocess.run(gpsbabel_cmd.split())

args = parse_arguments()

with open(args.fit_file_list.name, newline='') as fit_file_list:
	for fit_file in fit_file_list:
		fit_file_path = args.base_directory + fit_file
		unzipped_file = unzip_file(fit_file_path.strip())
		convert_fit_to_gpx(unzipped_file)