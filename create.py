#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys,os
import subprocess as sp

args = sys.argv[1:]
args = map(lambda s: s.lower(), args)
project = '_'.join(args)

cmd = 'ls .'
pipe = sp.Popen(cmd, shell=True, stdout=sp.PIPE)
out, err = pipe.communicate()
out = out.split()
dirs = filter(lambda s: s[0].isdigit(), out)
cur = max([int(x.split('_')[0]) for x in dirs])
next = str(cur+1)
project = next + '_' + project

cmd = 'mkdir %s' % project
os.system(cmd)

cmd = 'cp template.py %s/s1.py' % (project)
os.system(cmd)
