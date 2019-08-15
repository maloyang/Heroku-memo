# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import time
import requests
import logging

from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask, request, abort, render_template
from flask import json, jsonify
from flask_cors import CORS, cross_origin # for cross domain problem


app = Flask(__name__)
CORS(app)

#==== for Scheduler ====
def job_fun1():
    print('cron fun1')

def start_scheduler():
    scheduler = BackgroundScheduler()
    # run per minute
    scheduler.add_job(job_fun1, 'cron', second='0')
    # run per 10 seconds
    #scheduler.add_job(job_fun1, 'interval', seconds=10)

    # start the scheduler
    scheduler.start()


#==== web ====
@app.route('/')
def homepage():
    the_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
    return """
    <p>It is currently {time} in server side.</p>
    """.format(time=the_time)


def run_web():
    logging.info('starting web..')
    os.system('gunicorn -w 2 app:app')


if __name__ == "__main__":
    start_scheduler()
    run_web() #app.run()
