import bz2
import gzip
from pathlib import Path

path = "/Users/siddharthsoni/Downloads/generators-master/examples/www"
filepat = "access-log*"

def generator_file_opener(paths):
    for filename in paths:
        if filename.suffix == ".bz2":
            yield bz2.open(filename, "rt")
        elif filename.suffix == ".gz":
            yield gzip.open(filename, "rt")
        else:
            yield open(filename,"rt")

def gen_lines(log_file_handle):
    for each in log_file_handle:
        yield from each

def byte_col(obj):
    for each in obj:
        yield each.rsplit(None,1)[1]

def byte_sent(line):
    for each in line:
        yield int(each) if each != '-' else 0
# Generated via generator
log_file_names = Path(path).rglob(filepat)
log_file_handle = generator_file_opener(log_file_names)
log_lines = gen_lines(log_file_handle)
# ....
bytecol = byte_col(log_lines)
bytes = byte_sent(bytecol)
print("Total", sum(bytes))