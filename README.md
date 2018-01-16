# nagios-nrpe-memory-check
Simple Nagios memory check for Debian and Ubuntu

Compatible with Python2 and Python3.

## Usage
`./check_memory.py`

`MEMORY OK - 20420M available (63%) | 'available'=20420MB;;;0;32112`



`./check_memory.py -w 60 -c 90`

`MEMORY WARNING - 20383M available (63%) | 'available'=20383MB;;;0;32112`

## Installation 

* wget https://raw.githubusercontent.com/Benji81/nagios-nrpe-memory-check/master/check_memory.py 
* sudo mv check_memory.py /usr/lib/nagios/plugins
* Configure your nrpe and Nagios daemons