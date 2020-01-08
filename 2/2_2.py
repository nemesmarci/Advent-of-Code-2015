from common import boxes

print(sum(2 * (l + w) + l * w * h for l, w, h in boxes()))
