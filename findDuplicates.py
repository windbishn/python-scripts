entries = []
duplicate_entries = []
with open('connections.csv', 'r') as my_file:
    for line in my_file:
        columns = line.strip().split(',')
        if columns[0] not in entries:
            entries.append(columns[0])
        else:
            duplicate_entries.append(columns[0]) 

if len(duplicate_entries) > 0:
    with open('connections_out.csv', 'w') as out_file:
        with open('connections.csv', 'r') as my_file:
            for line in my_file:
                columns = line.strip().split(',')
                if columns[0] in duplicate_entries:
                    print line.strip()
                    out_file.write(line)
else:
    print "No repetitions"
