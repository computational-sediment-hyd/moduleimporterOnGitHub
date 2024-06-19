#!/usr/bin/env python
# coding: utf-8

import os
import tempfile
import urllib.request

def moduleimporterOnGitHub(url, cache=False, tmpfilename=None):
    # read raw data(binary) On Github
    with urllib.request.urlopen(url) as f: l = f.read() #.decode(encoding)  

    # file open & write data
    if tmpfilename is None:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.py', dir='.') as fp:
            fp.write(l)
        name = fp.name
    else:
        with open(tmpfilename, mode='wb') as f:
            f.write(l)
        name = tmpfilename
        
    # import 
    imp = __import__(os.path.basename(name)[:-3])
    
    # delete tmpfile
    if not cache : os.remove(name)
        
    return imp
