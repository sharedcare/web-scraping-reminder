#!/usr/bin/env python
#title           :periodic_task.py
#description     :Schedules given method and excutes task periodically.
#author          :Chen, Yizhen
#date            :Apr. 14, 2018
#version         :0.1.1
#python_version  :3.6.5 
#==============================================================================
from threading import Timer


class PeriodicTask(object):
    """Excutes task periodically 
    
    Attributes:
        interval: An integer defines time between every two tasks
        callback: A function handler represents the task to excute
        daemon: A boolean indicates if the task need to terminate manually 
        kwargs: An arguments handler represents 
                all parameters passing to the task
    """
    def __init__(self, interval, callback, daemon=True, **kwargs):
        """Inits PeriodicTask class with given parameters"""
        self.interval = interval
        self.callback = callback
        self.daemon   = daemon
        self.kwargs   = kwargs

    def run(self):
        """Runs the scheduler and excutes the task"""
        self.callback(**self.kwargs)
        t = Timer(self.interval, self.run)
        t.daemon = self.daemon
        t.start()

