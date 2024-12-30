from ._anvil_designer import dlugosc_faliTemplate
from anvil import *
import anvil.server


class dlugosc_fali(dlugosc_faliTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def calculate_click(self, **event_args):
    if (self.m.text >0 and self.n.text >0 ):
      self.data_choose_change()
      result = anvil.server.call("calculate_wave", self.m.text, self.n.text, self.is_lambda)
      self.result.text = f"Result: {result} {self.unit}"
    else:
      Notification("error").show()


  def data_choose_change(self, **event_args):
    # λ or f
    
    if self.data_choose.selected_value == "λ":
      self.is_lambda = True
      self.title.text = "Kalkulator długości emitowanego fotonu przez wodór"
      self.unit = "m"
    else: 
      self.is_lambda = False
      self.title.text = "Kalkulator częstotliwości emitowanego fotonu przez wodór"
      self.unit = "Hz"

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
