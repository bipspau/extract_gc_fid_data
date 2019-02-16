
# extract_GC_FID_data

This python script can be used to extract compound(s) of interest from the GC-FID data file
Note: if you use this script in your project, please cite this as 

Paudel Timilsena B, Seild-Adams I, Tumlinson JH . 2019. Herbivore-specific plant volatiles prime neighboring plants for non-specific defense responses. Paper submitted at New Phytologist.


### how to copy data file from GC-FID connected computer?

1. Copy all the data files in simple text format (not in word document).
2. This script extract information about the treatment, replication and time/date from the file name. Therefore make sure your file name contains these information separated by underscore (eg. 1_ctrl_04hr) 

### How to run this script in your computer? 
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