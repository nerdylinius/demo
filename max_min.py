records = []
while True:
    it = raw_input('Enter a number:')
    if it == 'done':
        break
    else:
        try:
            num = int(it)
        except ValueError, e:
            print 'Invalid input'
            continue
        records.append(num)
print 'Max is', max(records)
print 'Min is', min(records)
