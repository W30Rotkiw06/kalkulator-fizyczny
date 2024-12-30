from ._anvil_designer import dlugosc_faliTemplate
from anvil import *
import anvil.server


class dlugosc_fali(dlugosc_faliTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.lenght_or_freq = "długości"
    self.emmited_or_absorbed = "emitowanego"
    

    # Any code you write here will run before the form opens.

  def calculate_click(self, **event_args):
    if (self.m.text >0 and self.n.text >0 and self.m.text != self.n.text):
      self.data_choose_change()
      result = anvil.server.call("calculate_wave", self.m.text, self.n.text, self.is_lambda)
      self.result.text = f"Result: {result} {self.unit}"
    else:
      Notification("error").show()


  def data_choose_change(self, **event_args):
    # λ or f    
    if self.data_choose.selected_value == "λ":
      self.is_lambda = True
      self.lenght_or_freq = "długości"
      self.unit = "m"
    else: 
      self.is_lambda = False
      self.lenght_or_freq = "częstotliwości"
      self.unit = "Hz"
      
    self.title.text = f"Kalkulator {self.lenght_or_freq} {self.emmited_or_absorbed} fotonu przez wodór"

    

  def head_button_click(self, **event_args):
    open_form("home")

  def head_link_click(self, **event_args):
    open_form("home")

  def to_gravity_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("gravity_home")

  def to_atom_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("atomic_home")



  def m_n_change(self, **event_args):
    print("change", self.m.text, self.n.text )
    if (self.m.text is not None and self.n.text is not None):
      if self.m.text > self.n.text: 
        self.emmited_or_absorbed = "absorbowanego"
        self.hydrogen_image.source = "_/theme/hydrogen_abs.png"
      else:
        self.emmited_or_absorbed = "emitowanego"
        self.hydrogen_image.source = "_/theme/hydrogen_em.png"
    self.title.text = f"Kalkulator {self.lenght_or_freq} {self.emmited_or_absorbed} fotonu przez wodór"

      