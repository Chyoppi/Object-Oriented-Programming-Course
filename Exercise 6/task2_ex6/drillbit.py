class DrillBit:
    def __init__(self, diameter, max_rpm):
        self.diameter = diameter
        self.max_rpm = max_rpm

    def __str__(self):
        return f"DrillBit {self.diameter}mm, Max RPM: {self.max_rpm}"