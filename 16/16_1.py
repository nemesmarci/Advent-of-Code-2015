from aunts import read_data, RESULTS

aunts = read_data()

for aunt in aunts:
    match = True
    for item in RESULTS:
        if item not in aunts[aunt]:
            continue
        if RESULTS[item] != aunts[aunt][item]:
            match = False
            break
    if match:
        print(aunt)
        break
