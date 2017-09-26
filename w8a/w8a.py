#
# @file: w8a.py
# @author Marcus Edel
#
# Convert w8a and w8a.t to csv.
#
# Source: Fast training of support vector machines using sequential minimal
#         optimization by John C. Platt.
# Number of classes: 2
# Number of data: 49,749 / 14,951 (testing)
# Number of features: 300 / 300 (testing)
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

writeFile('w8a', 'w8a.csv', 300)
writeFile('w8a.t', 'w8a_t.csv', 300)
