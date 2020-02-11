#!/bin/env python3.7

count = 1
while count < 10:
    if count % 2 == 0:
        count += 1
        break
    print(f"We're counting odd numbers: {count}")
    count += 1
