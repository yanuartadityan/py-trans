"""class for defining stops"""

class Platform:
    def __init__(self, code=None, gps=None):
        self.code = code
        self.gps = gps

    def get_gps(self):
        return self.gps[0], self.gps[1]

class Stop(object):
    def __init__(self, name=None, num_platform=None):
        self.name = name
        self.num_platform = num_platform

    def get_name(self):
        return self.name

    def get_platform(self):
        return 