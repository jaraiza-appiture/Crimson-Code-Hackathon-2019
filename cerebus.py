# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 00:14:38 2019

@author: Brandon Townsend
"""

import subprocess
from subprocess import SubprocessError

class cerebus:
    
    lastdir = ""
    
    def __init__(self, path):
        self.proc = subprocess.Popen("ping" + str(self.lastdir), shell = True)
    
    def move(self, direction):
        
        if self.lastdir != direction: 
        
            if self.proc.poll() == None:
                try:
                    outs, errs = self.proc.communicate(timeout=15)
                except TimeoutExpired:
                    self.proc.kill()
                    outs, errs = self.proc.communicate()
                        
            self.lastdir = direction
            self.proc = subprocess.Popen("ping" + str(self.lastdir), shell = True)
            self.proc.call()
            
c = cerebus("www.google.com")

c.move("www.google.com")
            