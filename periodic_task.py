#!/usr/bin/env python
"""PeriodicTask class

Schedules given method and excutes task periodically 
"""
__author__ = 'Tony(Yizhen) Chen'
__version__ = '0.1.0'
__email__ = 'tony@sharedcare.io'

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
    def __init__(self, interval=60, callback, daemon=True, **kwargs):
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

