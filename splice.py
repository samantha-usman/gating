#Program to split segment list into individual segment files for analysis by Omicron
import fileinput
import numpy as np

#Counter for naming
counter = 1

#Loading .txt file containing start and end times for data segments
segment_file = np.genfromtxt("/home/samantha.usman/aligo/er8/omicron/segments/L1-SEGMENTS.txt", dtype = int)

#Looping over segment start end times
for line in segment_file:
        
        #Naming & saving to files
        if counter < 10:
                output_file = open("L1_segment_000%d.txt"%counter, "w")
                print >> output_file, line[0], line[1]
                output_file.close()
        elif counter < 100:
                output_file = open("L1_segment_00%d.txt"%counter, "w")
                print >> output_file, line[0], line[1]
                output_file.close()
        elif counter < 1000:
                output_file = open("L1_segment_0%d.txt"%counter, "w")
                print >> output_file, line[0], line[1]
                output_file.close()
        else:
                output_file = open("L1_segment_%d.txt"%counter, "w")
                print >> output_file, line[0], line[1]
                output_file.close()

        counter += 1
