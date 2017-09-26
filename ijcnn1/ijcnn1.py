#
# @file: ijcnn1.py
# @author Marcus Edel
#
# Convert ijcnn1 and ijcnn1.t to csv.
#
# Source: IJCNN 2001 neural network competition
# Number of classes: 2
# Number of data: 49,990 / 91,701 (testing)
# Number of features: 22
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

writeFile('ijcnn1.tr', 'ijcnn1_tr.csv', 22)
writeFile('ijcnn1.t', 'ijcnn1_t.csv', 22)
