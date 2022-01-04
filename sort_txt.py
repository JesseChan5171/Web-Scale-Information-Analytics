fn = 'Thecombine.txt'
sorted_fn = 'Thecombine_sort.txt'

with open(fn,'r') as first_file:
    rows = first_file.readlines()
    sorted_rows = sorted(rows, key=lambda x: int(x.split()[0]), reverse=False)
    with open(sorted_fn,'w') as second_file:
        for row in sorted_rows:
            second_file.write(row)
