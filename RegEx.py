import re


def subst(pattern, replace_str, string):
    x = re.sub(pattern, replace_str, string)
    return x


addr = ['100 NORTH MAIN ROAD',
        '100 BROAD ROAD APT.',
        'SAROJINI DEVI ROAD',
        'BROAD AVENUE ROAD']
new_address = []
for i in range(len(addr)):
    new_address.append(subst(" ROAD", " RD", addr[i]))
print(new_address)

