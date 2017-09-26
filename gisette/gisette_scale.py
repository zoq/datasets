#
# @file: gisette_scale.py
# @author Marcus Edel
#
# Convert gisette_scale and gisette_scale.t to csv.
#
# Source: http://www.nipsfsc.ecs.soton.ac.uk/datasets/
# Number of classes: 2
# Number of data: 6,000 / 1,000 (testing)
# Number of features: 5,000
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

writeFile('gisette_scale', 'gisette_scale.csv', 5000)
writeFile('gisette_scale.t', 'gisette_scale_t.csv', 5000)
