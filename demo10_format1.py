import math

radius = 3.0
area = (radius ** 2) * math.pi

print('radius=%f, area=%f' % (radius, area))
print('radius=%.3f, area=%.6f' % (radius, area))
print('radius=%(r)f, area=%(a)f' % {'r': radius, 'a': area})
print('radious={}, area={}'.format(radius, area))
print('radious={0}, area={1}'.format(radius, area))
print('radious={1}, area={0}'.format(area, radius))
print('radious={r}, area={a}'.format(r=radius, a=area))
print(f'radious={radius}, area={area}')
