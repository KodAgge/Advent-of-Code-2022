from common import load_file
import numpy as np

read_lines = load_file(test=True)
split_lines = [line.strip().split() for line in read_lines]
parsed_lines = [list(map(int,[l[6], l[12], l[18], l[21], l[27], l[30]])) for l in split_lines]