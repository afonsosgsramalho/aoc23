inputs, *blocks = open('day5.txt').read().split("\n\n")
inputs = list(map(int, inputs.split()[1::]))

seeds = [(inputs[i], inputs[i] + inputs[i + 1]) for i in range(0, len(inputs), 2)]

def part_one():
    for block in blocks:
        ranges = []

        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        
        new = []    
        for seed in seeds:
            for destination, source, length in ranges:
                if source <= seed < source + length:
                    new.append(destination + (seed - source))
                    break # we just need to found one particular correct option, then break
            else:
                new.append(seed)

        seeds = new
    
    return min(seeds)


for block in blocks:
    ranges = []

    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    
    new = []    
    while seeds:
        s, e = seeds.pop()
        for destination, source, length in ranges:
            os = max(s, source)
            oe = min(e, source + length)
            if os < oe:
                new.append((os - source + destination, oe - source + destination))
                if os > s:
                    seeds.append((s, os))
                if oe < e:
                    seeds.append((oe, e))
                break
        else:
            new.append((s, e))

    seeds = new

print(min(seeds)[0])