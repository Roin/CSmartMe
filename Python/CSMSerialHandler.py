import serial
import time
import string

class CSMSerialHandler:
  """Serial Connection Handler for our Smart Meter"""
  def __init__(self, device, baudrate):
    self.dev = device
    self.baud = baudrate
    
  def CSMConnect(self):
    self.s = serial.Serial(self.dev, self.baud, serial.SEVENBITS, serial.PARITY_EVEN, serial.STOPBITS_ONE, timeout=2)
    
  def CSMWrite(self, message):
    self.s.write(message)
    
  def CSMRead(self):
    return self.s.readline()
    
    
    