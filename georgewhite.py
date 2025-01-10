from hellokittyfamily import HelloKittyFamily

class GeorgeWhite(HelloKittyFamily):
    def __init__(self, job_title:str):
      super().__init__('Georgewhite', 'British', 'Adult father age', ['hard-working', 'supporting'])    
      self.job_title = job_title

    def __str__(self):
       return f'GeorgeWhite(job_title: {self.job_title})'

 
    def enjoy_outdoor_activity(self):
       return('Let\'s have fun!!')

    def work(self):
       return 'Let\'s work with George!'