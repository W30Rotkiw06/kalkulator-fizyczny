from ._anvil_designer import predkoscKosmicznaTemplate
from anvil import *
import anvil.server


class predkoscKosmiczna(predkoscKosmicznaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def calculate_click(self, **event_args):
    if(self.m1.text is not None and  self.m1_scinot is not None and self.r.text is not None and  self.r_scinot is not None and self.r.text > 0):
      m1 = self.m1.text * pow(10, self.m1_scinot.text)
      r = self.r.text * pow(10, self.r_scinot.text)
      velocity_number = int(self.wybor_predkosci.selected_value)
      velocity = anvil.server.call("calculate_orbit_escape_velocity", m1, r, velocity_number)
      self.result.text = f"Result: {velocity} m/s"
    else:
      Notification("error").show()

  def head_button_click(self, **event_args):
    open_form("home")

  def wybor_predkosci_change(self, **event_args):
    if self.wybor_predkosci.selected_value == "1":
      self.title.text = "Kalkulator pierwszej prędkości kosmicznej"
      self.speed_image.source = "_/theme/1predkosc.jpg"
    else:
      self.title.text = "Kalkulator drugiej prędkości kosmicznej"
      self.speed_image.source = "_/theme/2predkosc.jpg"
