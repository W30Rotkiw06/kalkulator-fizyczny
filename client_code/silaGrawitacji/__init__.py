from ._anvil_designer import silaGrawitacjiTemplate
from anvil import *
import anvil.server


class silaGrawitacji(silaGrawitacjiTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def calculate_click(self, **event_args):
    if(self.m1.text is not None and  self.m1_scinot is not None 
       and self.m2.text is not None and  self.m2_scinot is not None and 
       self.r.text is not None and  self.r_scinot is not None and self.r.text > 0):
      m1 = self.m1.text * pow(10, self.m1_scinot.text)
      m2 = self.m2.text * pow(10, self.m2_scinot.text)
      r = self.r.text * pow(10, self.r_scinot.text)
  
      gravity = anvil.server.call('calculate_gravitational_force', m1=m1, m2=m2, r=r)
      self.result.text = f"Result: {gravity} N"
    else:
      Notification("error").show()


    
    

  def head_button_click(self, **event_args):
    open_form('home')

