#!/usr/bin/env python3.7

# create a script that has single var I can set at top called USER

user = [{'admin': True, 'active': True, 'name': "Ana"},
    {'admin': False, 'active': True, 'Lilia':},
    {'admin': False, 'active': True , 'Edy':},
    {'admin': True, 'active': False, 'Edino':},
    {'admin': False, 'active': False, 'Perrito':}
]
line = 1

for user in users:
    prefix = f"{line}"

    if user['admin'] and user['active']:
        prefix = "ACTIVE - (ADMIN) "
    elif user['admin']:
        prefix = "(ADMIN) "
    elif user['active']:
        prefix = "ACTIVE - "

    print(prefix + user['name'])
    line += 1
