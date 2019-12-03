from aunts import read_data, RESULTS

aunts = read_data()

for aunt in aunts:
    match = True
    for item in RESULTS:
        if item not in aunts[aunt]:
            continue
        if ((item in ['cats', 'trees']
                and RESULTS[item] < aunts[aunt][item])
            or
           (item in ['pomeranians', 'goldfish']
               and RESULTS[item] > aunts[aunt][item])):
            continue
        elif RESULTS[item] != aunts[aunt][item]:
            match = False
            break
    if match:
        print(aunt)
        break
