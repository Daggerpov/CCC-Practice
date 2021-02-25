amount_bidders = int(input())

bids = {}

while True:
    try:
        name = input()
        amount = int(input())
    except:
        break
    bids[name] = amount
max = (-1, '')
for k, v in bids.items():
    if v > max[0]:
        max = v, k

if max[1] != '':
    print(max[1])