#
# @file: phishing.py
# @author Marcus Edel
#
# Convert phishing to csv.
#
# Source: https://archive.ics.uci.edu/ml/datasets/phishing+websites
# Number of classes: 2
# Number of data: 11,055
# Number of features: 68
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

writeFile('phishing', 'phishing.csv', 68)
