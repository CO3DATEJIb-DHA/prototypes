# -*- coding: utf-8 -*-
import logging


class SwitchManager:
    def __init__(self, config):
        self.logger = logging.getLogger("SwitchManager")
        self.config = config
        self.switches = {}

    def addSwitch(self, name, getFunction, setFunction, type=None):
        if name in self.switches:
            raise RuntimeError("Switch {0} already exists".format(name))

        self.switches[name] = {'set': setFunction, 'get': getFunction, 'type': type}

    def delSwitch(self, name):
        if name not in self.switches:
            raise RuntimeError("Wrong switch name: {0}".format(name))

        self.switches.pop(name)

    def setSwitchValue(self, name, value):
        if name not in self.switches:
            raise RuntimeError("Wrong switch name: {0}".format(name))

        switch = self.switches.get(name)
        switch['set'](name, value)

    def getSwitchValue(self, name):
        if name not in self.switches:
            raise RuntimeError("Wrong switch name: {0}".format(name))

        switch = self.switches.get(name)
        value = switch['get'](name)

        return value

    def start(self):
        self.logger.info("Starting")
        self.logger.info("Started")

    def stop(self):
        self.logger.info("Stopping")
        self.clearSwitches()
        self.logger.info("Stopped")

    def clearSwitches(self):
        self.logger.info("Clearing switches")
        self.switches.clear()

    def getStatus(self):
        switchStatus = {}

        for name, switch in self.switches.iteritems():
            switchStatus[name] = {'type': switch['type'], 'value': self.getSwitchValue(name)}

        return switchStatus


class SwitchCommandHandler:
    def __init__(self, switchManager):
        self.switchManager = switchManager

    def handleCommand(self, cmd, args):
        if cmd != 'switch':
            raise NotImplementedError("Wrong command: {0}".format(cmd))

        action = args.get('act')

        if action == 'set':
            name = args.get('name')
            value = args.get('value').lower()

            value = (value == '1' or value == 'true')

            self.switchManager.setSwitchValue(name, value)

            if args.get('_protocol', '') == 'udp':
                return {'_noAnswer': True}

            return True

        elif action == 'get':
            name = args.get('name')
            value = self.switchManager.getSwitchValue(name)
            return {'switchName': name, 'switchValue': value}

        elif action == 'status':
            return {'switchStatus': self.switchManager.getStatus()}

        elif action == 'start':
            self.switchManager.start()
            return True
        elif action == 'stop':
            self.switchManager.stop()
            return True

        else:
            raise NotImplementedError("Wrong action: {0}".format(action))
