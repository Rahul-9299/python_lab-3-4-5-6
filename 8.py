class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds  
    def __eq__(self, other):
        if isinstance(other, Time):
            return (self.hours == other.hours and
                    self.minutes == other.minutes and
                    self.seconds == other.seconds)
        return NotImplemented
    
ob1 = Time(10,20,30)
ob2 = Time(10,20,30)
print(ob1 == ob2) 