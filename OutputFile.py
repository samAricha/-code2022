from sqlalchemy import null


class OutputFile(object):
    nIntersections = null
    iSchedule = null
    def __init__(self):
        pass

    def output(self):
        pass


class ISchedule(object):
    def __init__(self, iNumber, incomingStreets, scheduleL):
        pass

class OrderNDuration(object):
    def __init__(self, sName, gDuration):
        pass