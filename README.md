extract_GC_FID_data

Python script written to extract compound(s) of interest from the GC-FID data file


# This script was used to extract compounds of interest from GC-FID.

### how to copy data file from GC-FID connected computer? ###

# Copy all the data files in simple text format (not in word document).
# make sure your datafile name has replication, treatment name and time/date of VOC collection 
# and separate each word in the file name by underscore (eg. 1_ctrl_04hr)

### How to run this script in your computer? ###
1. clone or download python script and save it in your working directory
2. open bash shell

If you are using mac:
	open terminal (go to application < utilities < terminal)

If you are using windows :
	go to run and type cmd and hit enter
	
3. set your working directory (make sure your python script is saved in your working directory)
Mac:
	cd Desktop/my_project
	
3. run python script 
Python extract_compounds_of_interest.py output_file_name.xls 

Then you will get a excel sheet that contains only the compounds of interest from all the data files. 	