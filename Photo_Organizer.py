import os
from PIL import Image

def getMonthName(month):
	if month == "01":
		return "January"
	elif month == "02":
		return "February"
	elif month == "03":
		return "March"
	elif month == "04":
		return "April"
	elif month == "05":
		return "May"
	elif month == "06":
		return "June"
	elif month == "07":
		return "July"
	elif month == "08":
		return "August"
	elif month == "09":
		return "September"
	elif month == "10":
		return "October"
	elif month == "11":
		return "November"
	elif month == "12":
		return "December"

		
def moveImage(path, year, month, day, cur_directory, cur_file):
	print()
	try:
		os.mkdir(year)
	except FileExistsError:
		pass
	os.chdir(cur_directory + "\\" + year)
	try:
		#print(month)
		os.mkdir(getMonthName(month))
	except:
		#print(month)
		pass
	os.chdir(cur_directory + "\\" + year + "\\" + getMonthName(month))
	name, extension = cur_file.split(".")
	os.rename(path, cur_directory + "\\" + year + "\\" + getMonthName(month) + "\\" + cur_file)

file_names = {i for i in os.listdir()}
cur_directory = os.getcwd()
print(file_names)
for cur_file in file_names:
	os.chdir(cur_directory)
	try:
		path = cur_directory + "\\" + cur_file
		print(Image.open(path)._getexif()[36867])
		info = Image.open(path)._getexif()[36867]
		date, time = info.split()
		#print(date)
		year, month, day = date.split(":")
		#print(year)
		#print(month)
		#print(day)
		moveImage(path, year, month, day, cur_directory, cur_file)
	except:
		print("File not an image")
		print()