#!/usr/bin/env python

import visa
from time import sleep

rm = visa.ResourceManager()
pwr = rm.open_resource('USB0::65535::37376::802243020737510059::0::INSTR')

# Show the device' ID string. Strip the extra \r\n at end of line.
print pwr.query('*IDN?').strip()

# Put device into remote control mode
pwr.write('SYST:REM')

# Set voltage to 5V
pwr.write('SOUR:VOLT 5.0')

# Set current to 1A
pwr.write('SOUR:CURR 1.0')

# Enable the output. Use '1' or 'ON' for enable.
print 'Enabling the output'
pwr.write('SOUR:OUTP 1')

sleep(2)

# Measure the Voltage
print 'Voltage =', pwr.query('MEAS:VOLT?').strip(), 'Volts'

# Measure the current
print 'Current =', pwr.query('MEAS:CURR?').strip(), 'Amps'

# Disable the output. Use '0' or 'OFF' for disable.
print 'Disabling the output'
pwr.write('SOUR:OUTP 0')

# Return the device to front-panel operation
pwr.write('SYST:LOC')

# Close the resource
pwr.close()
