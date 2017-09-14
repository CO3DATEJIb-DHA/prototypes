# -*- coding: utf-8 -*-

import logging
import socket
import alsaaudio
import threading
import Queue
import traceback


class UdpRecorder:
    def __init__(self):
        self.logger = logging.getLogger("UdpRecorder")

    def __str__(self):
        return str(self.addr)

    def start(self, host, port, sampleRate=8000, periodSize=100, channels=1, sampleFormat=alsaaudio.PCM_FORMAT_S16_LE):
        self.sentPackets = 0
        self.sentBytes = 0

        self.periodSize = periodSize
        self.addr = (host, port)
        self.sampleRate = sampleRate
        self.sampleFormat = sampleFormat
        self.channels = channels

        self.logger.info("{0} starting".format(self))

        self.logger.info("{0}: Creating socket".format(self))
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.settimeout(1)

        self.logger.info("{0}: Creating PCM capture".format(self))
        self.pcm = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)

        self.logger.info(
            "{0}: Setting playback parameters, channels: {1}, rate: {2}, period: {3}, format: {4}".format(
                self, self.channels, self.sampleRate, self.periodSize, self.sampleFormat))

        self.pcm.setchannels(self.channels)
        self.pcm.setrate(self.sampleRate)
        self.pcm.setformat(self.sampleFormat)
        self.pcm.setperiodsize(self.periodSize)

        self.queue = Queue.Queue()

        self.stopThread = False

        self.logger.info("{0}: Starting threads".format(self))

        self.sendThread = threading.Thread(target=self.sendThreadProc, name="UdpPlayerSendThread")
        self.recThread = threading.Thread(target=self.recThreadProc, name="UdpPlayerRecordThread")

        self.sendThread.daemon = True
        self.recThread.daemon = True

        self.sendThread.start()
        self.recThread.start()

        self.logger.info("{0} started".format(self))

    def stop(self):
        self.logger.info("{0} stopping".format(self))
        self.stopThread = True
        self.sendThread.join()
        self.recThread.join()

        self.socket.close()
        self.pcm.close()

        self.logger.info("{0} stopped".format(self))

    def status(self):
        if self.socket is None:
            return {'started': False}

        return {'started': True,
                'periodSize': self.periodSize,
                'addr': self.addr,
                'sampleRate': self.sampleRate,
                'sampleFormat': self.sampleFormat,
                'channels': self.channels,
                'sentPackets': self.sentPackets,
                'sentBytes': self.sentBytes}

    def sendThreadProc(self):
        while not self.stopThread:
            try:
                data = self.queue.get(True, 1)
                self.socket.sendto(data, self.addr)
                self.sentPackets += 1
                self.sentBytes += len(data)
            except Queue.Empty:
                pass
            except Exception as ex:
                self.logger.warning("Exception caught in send thread: {0}\n{1}".format(ex, traceback.format_exc()))

    def recThreadProc(self):
        while not self.stopThread:
            try:
                (length, data) = self.pcm.read()
                if length > 0:
                    self.queue.put(data)
            except Exception as ex:
                self.logger.warning("Exception caught in record thread: {0}\n{1}".format(ex, traceback.format_exc()))

