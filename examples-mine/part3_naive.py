import bz2,gzip


path = "/Users/siddharthsoni/Downloads/generators-master/examples/www"

from pathlib import Path

print(type(Path(path).rglob("access-log*")))
for filename in Path(path).rglob("access-log*"):
    if filename.suffix == ".bz2":
        wwwlog = bz2.open(filename,"rt")
    elif filename.suffix == ".gz":
        wwwlog = gzip.open(filename,"rt")
    else:
        wwwlog = open(filename)
    with open("access-log-bkp") as wwwlog:
        total = 0
    # for line in wwwlog:
    #     bytes_sent = line.rsplit(None,1)[1]
    #     if bytes_sent != '-':
    #         total += int(bytes_sent)
    # print("Total", total)