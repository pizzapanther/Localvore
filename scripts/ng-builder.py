#!/usr/bin/env python

from __future__ import print_function

import os
import time
import datetime
import subprocess

import pyinotify

class Compile (pyinotify.ProcessEvent):
  def __init__ (self, ngdir, *args, **kwargs):
    self.ngdir = ngdir
    self.ldir = os.path.join(self.ngdir, 'css')
    
    super(Compile, self).__init__(*args, **kwargs)
    
  def process_IN_CLOSE (self, event):
    build = False
    if event.mask == pyinotify.IN_CLOSE_WRITE:
      if event.pathname.endswith('.less'):
        self.less_compile()
        build = True
        
      elif event.pathname.endswith('.js'):
        build = True
        
      elif event.pathname.endswith('index.tpl.html'):
        build = True
        
    if build:
      self.build_html()
      
  def less_compile (self):
    print("Processing localvore.less " + unicode(datetime.datetime.now()))
    subprocess.call(
      "lessc {ldir}/localvore.less {ldir}/localvore.css".format(ldir=self.ldir),
      shell=True
    )
    
  def compile_all (self):
    self.less_compile()
    self.build_html()
    
  def build_html (self):
    tpl = os.path.join(self.ngdir, 'index.tpl.html')
    html = os.path.join(self.ngdir, 'index.html')
    
    ts = '?ts={}'.format(int(time.time()))
    
    fh = open(tpl, 'r')
    content = fh.read()
    fh.close()
    
    content = content.replace('[[ ts ]]', ts)
    
    fh = open(html, 'w')
    fh.write(content)
    fh.close()
    
def run_builder ():
  BASEDIR = os.path.abspath(os.path.dirname(__file__))
  os.chdir(BASEDIR)
  
  ngdir = os.path.join(BASEDIR, '..', 'ng-app')
  
  wm = pyinotify.WatchManager()
  handler = Compile(ngdir)
  handler.compile_all()
  notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
  wm.add_watch(ngdir, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
  notifier.loop()
  
if __name__ == "__main__":
  run_builder()
  