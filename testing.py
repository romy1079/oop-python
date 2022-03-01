class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <=+90):
            raise ValueError (f"Latitude { latitute } out of range")

        if not (-180 <= longitude <=+180):
            raise ValueError (f"longitude { longitude} out of range")

        self.latitude = latitude
        self.longitude = longitude

        @property
        def latitude(self):
            return self._latitude

        @property
        def longitude(self):
            return self._longitude

    def __repr__(self):
        return f" {self.latitude} S, {self.longitude} E"

    def __str__(self):
        return f" {self.latitude} S, {self.longitude} E"


if __name__ != "main":
    pass
else:
    Position(-70, 10)

print( position )