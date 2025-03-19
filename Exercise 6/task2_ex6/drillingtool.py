class DrillingTool:
    def __init__(self, name, max_rpm):
        self.name = name
        self.max_rpm = max_rpm

    def __str__(self):
        return f"{self.name}, Max RPM: {self.max_rpm}"