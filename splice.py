#Program to split segment list into individual segment files for analysis by Omicron
import fileinput
import numpy as np

#Counter for naming
counter = 1

#Loading .txt file containing start and end times for data segments
segment_files = {}
segment_files['H1'] = np.genfromtxt("/home/samantha.usman/aligo/er8b/omicron/segments/L1-SEGMENTS.txt", dtype = int)
segment_files['L1'] = np.genfromtxt("/home/samantha.usman/aligo/er8b/omicron/segments/H1-SEGMENTS.txt", dtype = int)

for ifo in segment_files.keys():
        #Looping over segment start end times
        counter = 0
        for line in segment_files[ifo]:
                #Naming & saving to files
                if counter < 10:
                        output_file = open("%s_segment_000%d.txt" % (ifo,counter), "w")
                        print >> output_file, line[0], line[1]
                        output_file.close()
                elif counter < 100:
                        output_file = open("%s_segment_00%d.txt" % (ifo,counter), "w")
                        print >> output_file, line[0], line[1]
                        output_file.close()
                elif counter < 1000:
                        output_file = open("%s_segment_0%d.txt" % (ifo,counter), "w")
                        print >> output_file, line[0], line[1]
                        output_file.close()
                else:
                        output_file = open("%s_segment_%d.txt" % (ifo,counter), "w")
                        print >> output_file, line[0], line[1]
                        output_file.close()
                counter += 1
