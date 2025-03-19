from drill import Drill

class CordlessDrill(Drill):
    def __init__(self, manufacturer, model, rpm):
        super().__init__(manufacturer, model, rpm, max_diameter=10)