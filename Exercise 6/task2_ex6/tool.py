class Tool:
    def __init__(self, manufacturer:str, model:str, rpm:int):
        self.manufacturer = manufacturer
        self.model = model
        self.rpm = rpm

    def __str__(self):
        return f"{self.manufacturer} {self.model}, Max RPM: {self.rpm}"