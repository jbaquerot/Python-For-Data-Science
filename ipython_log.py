# IPython log file

import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt' 
records = [json.loads(line) for line in open(path)]
import json
path = 'ch2/usagov_bitly_data2012-03-16-1331923249.txt' 
records = [json.loads(line) for line in open(path)]
import json
path = 'ch2/usagov_bitly_data2012-11-13-1352840290.txt'
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
get_ipython().magic(u'logstart')
ip_info = get_ipython().getoutput(u'ifconfig eth0 | grep "inet "')
ip_info[0].strip()
ip_info = get_ipython().getoutput(u'ifconfig en0 | grep "inet "')
ip_info[0].strip()
ip_info = get_ipython().getoutput(u'ifconfig en1 | grep "inet "')
ip_info[0].strip()
pdc
get_ipython().magic(u'debug')
def f(x, y, z=1):
    tmp = x + y
    return tmp / z
get_ipython().magic(u'debug (f, 1, 2, z = 3)')
get_ipython().magic(u'debug (f, 1, 2, z = 3)')
get_ipython().magic(u'debug (f, 1, 2, z = 3)')
def set_trace():
    from IPython.core.debugger import Pdb
    Pdb(color_scheme='Linux').set_trace(sys._getframe().f_back)
    
def debug(f, *args, **kwargs):
    from IPython.core.debugger import Pdb
    pdb = Pdb(color_scheme='Linux')
    return pdb.runcall(f, *args, **kwargs)
debug (f, 1, 2, z = 3)
set_trace()
class Message:
    def __init__(self, msg):
        self.msg = msg
class Message:
    def __init__(self, msg):
        self.msg = msg
    def __repr__(self):
        return 'Message: %s' % self.msg
x = Message('I have a secret')
x
