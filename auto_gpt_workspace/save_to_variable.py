import json
import subprocess

output = subprocess.check_output(['read_file', '--filename', 'river_summary.txt'])
output = output.decode('utf-8')

with open('output_variable.txt', 'w') as f:
    f.write(json.dumps({'output': output}))
