# This script was used to extract compounds of interest from GC-FID.

###### how to copy data file from GC-FID connected computer? ######
# Copy all the data files in simple text format (not in word document).
# make sure your datafile name has replication, treatment name and time/date of VOC collection 
# and separate each word in the file name by underscore (eg. 1_ctrl_04hr)

#### How to run this script in your computer? ####
MAc - #application > utility > terminal
Window - 

#!/usr/bin/env python
import os, sys, re

fileout = sys.argv[1]
file_o = open(fileout, "w")
col1 = "Treatment"
col2 = "Replication"
col3 = "Time_after_exposure"
col4 = "Compound_name"
col5 = "Retention_peak"
col6 = "Area"
col7 = "Quantity"

file_o.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" %(col1, col2, col3, col4, col5,col6,col7))

# give path of the datafile

os.chdir("20170821_voc_absorption_and_reemission")

x = 0;	
for cur_file in os.listdir("."):
	if cur_file.endswith(".txt"):
		heading = cur_file[:-4]
		parts = heading.split("_")
		#print parts
		rep = parts[0]
		tret = parts[1]
		tae = parts[2]
		#print rep + " and " + tret

	
		x = x + 1    
		dict  = {}   
        for all_text in open(cur_file, "r"):
            line = all_text.strip().split("\t")
            if "".join(line).startswith("Signal"):
                continue
            elif len(line) > 4:
                print line 
                retn = float(line[1])
                area = str(line[4]) 
                #print retn
                #print area
    
  # to extract compound of interest from the data files
    
                if (retn >= 4.10 and retn <= 4.17):
                    dict["Propyl aldoxime, 2 methyl-,syn-"] = str(retn) + "\t"  + str(area)
                elif (retn >= 4.23 and retn <= 4.29):
                    dict["Propyl aldoxime, 2 methyl-,anti-"] = str(retn) + "\t"  + str(area)
                elif (retn >= 5.07 and retn <= 5.13):
                    dict["Z3-Hexenal"] = str(retn) + "\t"  + str(area)
                elif (retn >= 6.54 and retn <= 5.57):
                    dict["E2-Hexenal"] = str(retn) + "\t"  + str(area)
                elif (retn >= 6.58 and retn <= 6.63):
                    dict["Z3-Hexenol"] = str(retn) + "\t"  + str(area)
                elif (retn >= 6.69 and retn <= 6.79):
                    dict["Butyl aldoxime, 2 methyl-,syn-"] = str(retn) + "\t"  + str(area)
                elif (retn >= 6.86 and retn <= 6.96):
                    dict["Butyl aldoxime, 2 methyl-,anti-"] = str(retn) + "\t"  + str(area)
                elif (retn >= 7.90 and retn <= 7.96):
                    dict["Unknown_1"] = str(retn) + "\t"  + str(area)
                elif (retn >= 9.01 and retn <= 9.07):
                    dict["a-Pinene"] = str(retn) + "\t"  + str(area)
                elif (retn >= 10.41 and retn <= 10.47):
                    dict["Sabinene"] = str(retn) + "\t"  + str(area)
                elif (retn >= 10.49 and retn <= 10.55):
                    dict["B-Pinene"] = str(retn) + "\t"  + str(area)
                elif (retn >= 11.10 and retn <= 11.16):
                    dict["Myrcene"] = str(retn) + "\t"  + str(area)
                elif (retn >= 11.71 and retn <= 11.77):
                    dict["Z3-Hexenyl acetate"] = str(retn) + "\t"  + str(area)
                elif (retn >= 12.05 and retn <= 12.11):
                    dict["E2 Hexenyl acetate"] = str(retn) + "\t"  + str(area)
                elif (retn >= 12.39 and retn <= 12.45):
                    dict["Limonene"] = str(retn) + "\t"  + str(area)
                elif (retn >= 12.48 and retn <= 12.54):
                    dict["1,8-Cineole"] = str(retn) + "\t"  + str(area)
                elif (retn >= 13.16 and retn <= 13.22):
                    dict["E-b-Ocimene"] = str(retn) + "\t"  + str(area)
                elif(retn >= 15.02 and retn <= 15.06):
                    dict["Linalool"] = str(retn) + "\t"  + str(area)
                elif(retn >= 15.20 and retn <= 15.26):
                    dict["Nonanal"] = str(retn) + "\t"  + str(area)
                elif (retn >= 21.70 and retn <= 21.76):
                    dict["Indole"] = str(retn) + "\t"  + str(area)
                elif (retn >= 22.35 and retn <= 22.41):
                    dict["Nonyl_acetate"] = str(retn) + "\t"  + str(area)
                    nony = float(area)
                elif (retn >= 22.78 and retn <= 22.83):
                    dict["Z3 Hexenyl tilgate"] = str(retn) + "\t"  + str(area)
                elif (retn >= 23.40 and retn <= 23.46):
                    dict["Nicotine"] = str(retn) + "\t"  + str(area)
                elif (retn >= 25.14 and retn <= 25.20):
                    dict["E or Z Jasmone"] = str(retn) + "\t"  + str(area)
                elif (retn >= 26.28 and retn <= 26.36):
                    dict["E-a-Bergamotene"] = str(retn) + "\t"  + str(area)
                elif (retn >= 26.51 and retn <= 26.57):
                    dict["Unknown ST 1"] = str(retn) + "\t"  + str(area)
                elif (retn >= 26.93 and retn <= 26.99):
                    dict["E-b-Farnesene"] = str(retn) + "\t"  + str(area)
                elif (retn >= 27.70 and retn <= 27.76):
                    dict["Aristolochene(4,4-di epi)"] = str(retn) + "\t"  + str(area)
                elif (retn >= 27.78 and retn <= 27.83):
                    dict["Unknown ST 2"] = str(retn) + "\t"  + str(area)
                elif (retn >= 28.48 and retn <= 28.54):
                    dict["B-Bisabolene"] = str(retn) + "\t"  + str(area)
                elif (retn >= 28.93 and retn <= 28.99):
                    dict["B-Sesquiphellandrene"] = str(retn) + "\t"  + str(area)
                
                
            #print dict

        for i in dict:
            retn_new = float(dict[i].split("\t")[0])
            #print retn_new
            area_new = float(dict[i].split("\t")[1])

# calculate amount of compounds by comparing peak area of compound of interest with the peak area of internal standard.
# we used 120ul of elution buffer which contains 480ng of internal standard. 

            quantity = float(area_new * 480 / nony)
            print ("%s = %s, %s = %s, %s = %f, %s = %f, %s = %f" 
            %(col1, heading, col2, i, col3, retn_new, col4, area_new, col5, quantity))
            #print heading, i, retn_new, area_new, quantity
            file_o.write("%s\t%s\t%s\t%s\t%.2f\t%.0f\t%.2f\n" %(tret, rep, tae, i, retn_new, area_new, quantity))
            #file_o.write("\n")


file_o.close()
