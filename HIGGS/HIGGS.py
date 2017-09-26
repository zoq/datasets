#
# @file: HIGGS.py
# @author Marcus Edel
#
# Convert HIGGS to csv and create a training and test set.
#
# Source: https://archive.ics.uci.edu/ml/datasets/HIGGS
# Number of classes: 2
# Number of data: 11,000,000
# Number of features: 28
#
import re

def writeFile(inputfile, outpufile, instances, size):
  wf = open(outpufile, 'w')
  counter = 0
  values = [0.0] * (instances + 1)

  with open(inputfile) as rf:
    for line in rf:
      if counter < size[0]:
        counter += 1
        continue

      if size[1] != -1 and counter > size[1]:
        break

      matches = re.findall('(\d+):(\d+)', line, re.DOTALL)
      values[-1] = int(line[0])

      for index, value in matches:
        values[int(index) - 1] = float(value)

      wf.write(','.join(map(str, values)) + '\n')
      values = [0.0] * (instances + 1)
      counter += 1
  wf.close()

writeFile('HIGGS', 'HIGGS.csv', 28, (0, 11000000 - 500000))
writeFile('HIGGS', 'HIGGS_t.csv', 28, (11000000 - 500000, -1))
