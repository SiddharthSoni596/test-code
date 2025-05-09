# Sum up the bytes transferred in an Apache server log using


# open the file
# Read line by line
# sum up last bytes sizes
# Total 230741830

with open("access-log-bkp") as wwwlog:
    total = 0
    for line in wwwlog:
        bytes_sent = line.rsplit(None,1)[1]
        if bytes_sent != '-':
            total += int(bytes_sent)
    print("Total", total)
