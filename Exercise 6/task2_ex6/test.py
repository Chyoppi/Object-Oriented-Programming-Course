from cordlessdrill import CordlessDrill
from drillbit import DrillBit

if __name__ == "__main__":
    drill = CordlessDrill("Porakone", "X100", 1500)
    print(drill)

    bit1 = DrillBit(8, 2000)  # Valid for cordless drill
    bit2 = DrillBit(12, 2000)  # Too large for cordless drill

    drill.attach_drill_bit(bit1)  # Should work
    drill.attach_drill_bit(bit2)