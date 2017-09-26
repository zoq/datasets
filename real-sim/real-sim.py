#
# @file: real-sim.py
# @author Marcus Edel
#
# Convert real-sim to csv.
#
# Source: https://people.cs.umass.edu/~mccallum/code-data.html
# Number of classes: 2
# Number of data: 72,309
# Number of features: 20,958
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

writeFile('real-sim', 'real-sim.csv', 20958)
