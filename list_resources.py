#!/usr/bin/env python

"""Lists all the VISA instruments we can find"""

import visa
rm = visa.ResourceManager()
for line in rm.list_resources():
    print line
