#!/usr/bin/python2
# -*- coding: utf-8 -*-

import socket
import pygame 
import logging 
import logging.config
import os
import signal
import sys
import argparse
import json
import traceback

from PyQt4.QtCore import QTimer
from PyQt4.QtGui import QApplication

path = os.path.realpath(__file__)
dir = os.path.dirname(path)
os.chdir(dir)

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", default="./config.conf", help="Config file location")

args = vars(parser.parse_args())

config = {}

with open(args['config'], 'r') as configFile:
    config = json.load(configFile)

logConfig = config['Logging'];
logConfig['version'] = 1;
logging.config.dictConfig(logConfig);

logger = logging.getLogger("Main")

try:
    logger.info("New instance started with command line {0}".format(sys.argv));
    config = config['Settings']

    logger.info("Args is {0}".format(args))
    logger.info("Config is {0}".format(config))

    for (name, value) in args.iteritems():
        if value is not None:
            config[name] = value

    logger.info("Effective config is {0}".format(config))

    logger.debug("Creating Qt app")
    app = QApplication(sys.argv)

    signal.signal(signal.SIGINT, lambda *a: QApplication.quit())    
    signal.signal(signal.SIGTERM, lambda *a: QApplication.quit())    
    
    timer = QTimer()
    timer.start(500)  # You may change this if you wish.
    timer.timeout.connect(lambda: None)  # Let the interpreter run each 500 ms.    
    
    pygame.init()

    ###
    
    socket.setdefaulttimeout(config['System']['socketTimeout'])
    
    from CamViewWidget import*
    from ControlWidget import*
    from SoundWidget import*
    from client import VideoClient, ControlClient, ServoClient, SwitchClient, SoundClient, TankClient
    
    from client import JoystickManager

    host, port = config['Server']['host'], int(config['Server']['port'])

    #tankClient = TankClient((host, port))
    #tankClient.start()
    #tankClient.reset()

    videoClient = VideoClient((host, port))
    videoClient.start()
    servoClient = ServoClient((host, port))
    servoClient.start()
    switchClient = SwitchClient((host, port))
    switchClient.start()
    soundClient = SoundClient((host, port))
    soundClient.start()

    joyUpdateInterval = float(config['Joystick']['interval'])
    joystickManager = JoystickManager(joyUpdateInterval)
    joystickManager.start()
    
    controlCfg = config['Control']
    
    controlClient = ControlClient(joystickManager, servoClient, switchClient, controlCfg)
    controlClient.start()

    videoWnd = CamViewWidget(videoClient)
    controlWnd = ControlWidget(controlClient)
    soundWnd = SoundWidget(soundClient)
    
    videoWnd.setWindowTitle("Video")
    controlWnd.setWindowTitle("Control")
    soundWnd.setWindowTitle("Sound")
    
    videoWnd.show()
    controlWnd.show()
    soundWnd.show()
    
    ###

    logger.debug("Starting Qt app")
    res = app.exec_()
    
    videoWnd.close()
    controlWnd.close()
    soundWnd.close()

    controlClient.stop()
    joystickManager.stop()
    videoClient.stop()
    servoClient.stop()
    switchClient.stop()
    soundClient.stop()
    #tankClient.stop()
    
    pygame.quit()
    logger.info("Instance ended")
    sys.exit(res) 

except Exception, ex:
    logger.error("Exception caught: {0}\n{1}".format(ex, traceback.format_exc()))
