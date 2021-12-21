
# i totally cheated on this one
# I tried to use the acceleration formulas with gravity set to 1, but I could not get the math to work
# It is more likely that I could not understand the formulas and use them correctly
# https://opentextbc.ca/openstaxcollegephysics/chapter/projectile-motion/ is what I used to try to figure this out
# gravity (g) is constant at -1
# each step (or second) distance traveled is 
# 
t = -1e99
for initial_velocity in range(91,500):
    l = set()
    y = 0
    steps = 0
    while 1:
        y += initial_velocity
        initial_velocity -= 1
        l.add(y)
        if -53 >= y >= -92:
            print('in the target area')
            t = max(t, max(l))
            print(f'steps is {steps}')
            break
        if y < -92:
            # print('overshot')
            break
        steps += 1
print(f'max height is {t}')