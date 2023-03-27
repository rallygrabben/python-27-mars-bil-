class Bil:
    
    # constructor körs först
    def __init__(self, fabrikat, color, lager):
        self.fabrikat = fabrikat
        self.color = color
        self.lager = lager

    def getFabrikat(self):
        return self.fabrikat 
