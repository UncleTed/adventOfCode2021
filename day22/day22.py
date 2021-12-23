
# on x=10..12,y=10..12,z=10..12

from typing import Counter


def make_range(r):
    begin_end = r.split('=')[1].split('..')
    return range(int(begin_end[0]), int(begin_end[1])+1)

with open("./long.txt") as f:
    c = Counter()
    for line in f:
        on_off = line[:3]
        x, y, z = line[3:].split(',')
        x_range = make_range(x)
        y_range = make_range(y)
        z_range = make_range(z)
        
        # if x_range.start >= -50 and x_range.stop <= 51 and y_range.start >= -50 and y_range.stop <= 51 and z_range.start >= -50 and z_range.stop <= 51:
           
        print(x_range, y_range, z_range)
        if on_off == 'on ':
            for x in x_range:
                for y in y_range:
                    for z in z_range:
                        c[x,y,z] = 1

        else:
            for x in x_range:
                for y in y_range:
                    for z in z_range:
                        c[x,y,z] = 0
        # else:
        #     print(x_range, y_range, z_range)
    print(sum(c.values()))