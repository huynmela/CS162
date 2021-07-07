# Author: Melanie Huynh
# Date: 2/3/2021
# Description:

import json

class SatData:
    def __init__(self):
        """
        Initializes the SatData object and reads in the .json file
        """
        with open("sat.json", "r") as infile:
            self._sat = json.load(infile)["data"]
        #Define the headers for the csv
        self._headers = ["DBN", "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]

    def save_as_csv(self, DBNs):
        """
        This method takes a list of district bureau numbers and saves a CSV file
        """
        with open("output.csv", "w") as outfile:
            # create the headers
            for i in range(0, 5):
                outfile.write(self._headers[i] + ",") # delimits header names

            # moves to next line
            outfile.write(self._headers[5] + "\n")

            # populates information
            for data in self._sat:
                if data[8] in DBNs:
                    outfile.write(data[8] + ",")
                    if "," in data[9]:
                        outfile.write("\""+data[9]+"\"" + ",")
                    else:
                        outfile.write(data[9] + ",")
                    outfile.write(",".join([data[i] for i in range(10,14)]) + "\n")

#TESTING
sd = SatData()
dbns = ["03M299", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)
