#
# @file: abalone.py
# @author Marcus Edel
#
# Convert covtype.binary to csv.
#
# Source: http://archive.ics.uci.edu/ml/datasets/Abalone
# Number of classes: 2
# Number of data: 4177
# Number of features: 8
#
import re

def writeFile(inputfile, outpufile, instances):
  wf = open(outpufile, 'w')

  values = [0.0] * (instances + 1)
  with open(inputfile) as rf:
    for line in rf:
      line = line.split(',')
      values[-1] = 0 if line[0] == 'M' else 1
      values[0:-1] = [float(d) for d in line[1:]]

      wf.write(','.join(map(str, values)) + '\n')
      values = [0.0] * (instances + 1)
  wf.close()

writeFile('abalone.data', 'abalone.csv', 8)
