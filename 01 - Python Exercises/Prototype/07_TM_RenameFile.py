import os

path        = 'C:\\Users\\Me\\Downloads\\'
filename    = 'District_Performance.csv'
fileNumber  = "15";
newFileName = 'District_Performance_' + fileNumber + '.csv'

os.rename( path + filename, path + newFileName )