from tool import Tool

class Drill(Tool):
    
    def __init__(self, manufacturer, model, rpm, max_diameter):
        super().__init__(manufacturer, model, rpm)
        self.max_diameter = max_diameter
        self.attached_bit = None

    def attach_drill_bit(self, drill_bit):
        if drill_bit.diameter > self.max_diameter:
            print(f"Error: {drill_bit.diameter}mm bit is too large for this drill (Max {self.max_diameter}mm).")
            return
        if drill_bit.max_rpm < self.rpm:
            print(f"Error: Drill RPM exceeds the max RPM of the bit ({drill_bit.max_rpm} RPM).")
            return
        
        self.attached_bit = drill_bit
        print(f"Attached {drill_bit} to {self.model}.")

    def __str__(self):
        return f"{super().__str__()}, Max Bit Diameter: {self.max_diameter}mm"