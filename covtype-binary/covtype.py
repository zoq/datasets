#
# @file: covtype.py
# @author Marcus Edel
#
# Convert covtype.binary to csv.
#
# Source: https://archive.ics.uci.edu/ml/datasets/covertype
# Number of classes: 2
# Number of data: 581,012
# Number of features: 54
#
import re

def writeFile(inputfile, outpufile, instances):
  wf = open(outpufile, 'w')

  values = [0.0] * (instances + 1)
  with open(inputfile) as rf:
    for line in rf:
      matches = re.findall('(\d+):(\d+)', line, re.DOTALL)
      values[-1] = 0 if line[0] == '1' else 1

      for index, value in matches:
        values[int(index) - 1] = float(value)

      wf.write(','.join(map(str, values)) + '\n')
      values = [0.0] * (instances + 1)
  wf.close()

writeFile('covtype.libsvm.binary', 'covtype_binary.csv', 54)
