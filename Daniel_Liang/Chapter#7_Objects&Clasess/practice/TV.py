class TV:

    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False


    def getOnStatus(self):
        return self.on
    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel

    def getVolumeLevel(self):
        return self.volumeLevel

    def setVolumeLevel(self, volume):
        if self.on and 1 <= self.volumeLevel <= 7:
            self.volumeLevel = volume

    def channelUp(self):
        if self.on and self.volumeLevel < 120:
            self.volumeLevel += 1

    def channelDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1


    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self):
        if self.on and self.volumeLevel > 1:
            self.volumeLevel -= 1
