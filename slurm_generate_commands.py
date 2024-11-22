import sys
import math
from pathlib import Path

input_file = sys.argv[1]
n_processes = int(sys.argv[2])
name = Path(input_file).stem
output_prefix = f"output/{name}"

with open(input_file) as fh:
    total_lines = len(fh.readlines())

# n_processes = 4
lines_per_process = math.ceil(total_lines / n_processes)
for offset in range(0, total_lines, lines_per_process):
    end_offset = min(total_lines, offset+lines_per_process)
    output_file = f"{output_prefix}_{offset:05d}_{end_offset:05d}.npy"
    print(f"--start_offset {offset} --end_offset {offset+lines_per_process} {input_file} {output_file}")
