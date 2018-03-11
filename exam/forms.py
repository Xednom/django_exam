class EdiWowForm():  # try to load this thru forms
    a = ['edi', 'wow', 'edi wow']
    for n, i in enumerate(range(17)):
        if i % 3 == 0 and i % 5 == 0:
            print a[2]
        elif i % 3 == 0:
            print a[0]
        elif i % 1 == 0:
            print n
        elif i % 5 == 0:
            print n, a[1]
