#!/usr/bin/env python
# coding: utf-8

import os
import tempfile
import urllib.request

def moduleimporterOnGitHub(url, cache=False):
    # read raw data(binary) On Github
    with urllib.request.urlopen(url) as f: l = f.read() #.decode(encoding)  
        
    # make tmpfile
    d, name = tempfile.mkstemp(suffix='.py', dir='.')
    # write date
    os.write(d, l)
    # close system
    os.close(d)
    
    # import 
    imp = __import__(os.path.basename(name)[:-3])
    
    # delete tmpfile
    if not cache : os.remove(name)
        
    return imp

