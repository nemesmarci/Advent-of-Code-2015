from common import get_data

_, molecule = get_data()


print(sum(1 for c in molecule if c.isupper())
      - molecule.count('Rn')
      - molecule.count('Ar')
      - 2 * molecule.count('Y')
      - 1)
