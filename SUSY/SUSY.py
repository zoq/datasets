#
# @file: SUSY.py
# @author Marcus Edel
#
# Convert SUSY to csv and create a training and test set.
#
# Source: https://archive.ics.uci.edu/ml/datasets/SUSY
# Number of classes: 2
# of data: 5000000
# of features: 18
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

writeFile('SUSY', 'SUSY.csv', 18, (0, 5000000 - 500000))
writeFile('SUSY', 'SUSY_t.csv', 18, (5000000 - 500000, -1))
