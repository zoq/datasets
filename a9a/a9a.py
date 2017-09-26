#
# @file: a9a.py
# @author Marcus Edel
#
# Convert a9a and a9a.t to csv.
#
# Source: https://archive.ics.uci.edu/ml/datasets/adult
# Number of classes: 2
# Number of data: 32,561 / 16,281 (testing)
# Number of features: 123 / 123 (testing)
#
import re

def writeFile(inputfile, outpufile, instances):
  wf = open(outpufile, 'w')

  values = [0.0] * (instances + 1)
  with open(inputfile) as rf:
    for line in rf:
      matches = re.findall('(\d+):(\d+)', line, re.DOTALL)
      values[-1] = 0 if line[0] == '-' else 1

      for index, value in matches:
        values[int(index) - 1] = float(value)

      wf.write(','.join(map(str, values)) + '\n')
      values = [0.0] * (instances + 1)
  wf.close()

writeFile('a9a', 'a9a.csv', 123)
writeFile('a9a.t', 'a9a_t.csv', 123)
