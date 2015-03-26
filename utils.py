
from datetime import tzinfo
from datetime import timedelta


class GMT1(tzinfo):

    def utcoffset(self,dt):
        return timedelta(hours=1,minutes=00)

    def tzname(self,dt):
        return " GMT+01:00"

    def dst(self,dt):
        return timedelta(0)