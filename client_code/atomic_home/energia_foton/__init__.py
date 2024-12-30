from ._anvil_designer import energia_fotonTemplate
from anvil import *
import anvil.server


class energia_foton(energia_fotonTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def calculate_click(self, **event_args):
    if (
      self.lambda_f.text is not None
      and self.lambda_f_scinot is not None
      and self.lambda_f.text > 0):

      self.is_lambda = True if self.data_choose.selected_value == "λ" else False

      self.unit_multiplicator = 1
      if self.unit_choose.selected_value == "eV":
        self.unit_multiplicator = 1/( 1.6 * pow(10, -19))
      
      
      if (self.is_lambda):
        c = 3 * pow(10, 8)
        
        f = c/(self.lambda_f.text * pow(10, self.lambda_f_scinot.text))
      else: 
        f = self.lambda_f.text * pow(10, self.lambda_f_scinot.text)
        
      energy = anvil.server.call(
        "calculate_photon_energy", f, self.unit_multiplicator
      )
      self.result.text = f"Result: {energy} {self.unit_choose.selected_value}"
    else:
      Notification("error").show()

  def head_button_click(self, **event_args):
    open_form("home")

  def unit_choose_change(self, **event_args):
    # eV or J
    self.unit_multiplicator = 1
    if self.unit_choose.selected_value == "eV":
      self.unit_multiplicator = 1/( 1.6 * pow(10, -19))

  def data_choose_change(self, **event_args):
    # λ or f
    
    if self.data_choose.selected_value == "λ":
      self.lambda_f_label.text = "λ [m]"
      self.is_lambda = True 
    else: 
      self.lambda_f_label.text = "f [Hz]"
      self.is_lambda = False
      

  def head_link_click(self, **event_args):
    open_form("home")

  def to_gravity_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("gravity_home")
    
  def to_atom_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('atomic_home')


