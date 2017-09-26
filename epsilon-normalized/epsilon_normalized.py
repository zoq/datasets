#
# @file: epsilon_normalized.py
# @author Marcus Edel
#
# Convert epsilon_normalized and epsilon_normalized.t to csv.
#
# Source: http://largescale.ml.tu-berlin.de/summary/
# Number of classes: 2
# Number of data: 400,000 / 100,000 (testing)
# Number of features: 2,000
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

writeFile('epsilon_normalized', 'epsilon_normalized.csv', 2000)
writeFile('epsilon_normalized.t', 'epsilon_normalized_t.csv', 2000)
