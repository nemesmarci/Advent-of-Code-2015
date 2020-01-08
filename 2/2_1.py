from common import boxes

print(sum(3 * l * w + 2 * w * h + 2 * h * l for l, w, h in boxes()))
