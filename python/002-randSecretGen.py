#!/usr/bin/env python3.7

import secrets
import string

alphabet = string.ascii_letters + string.digits
passwd = ''.join(secrets.choice(alphabet) for i in range(32))
f = passwd
