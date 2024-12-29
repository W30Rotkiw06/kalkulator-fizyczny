from ._anvil_designer import grawitacjaTemplate
from anvil import *
import anvil.server


class grawitacja(grawitacjaTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def calculate_click(self, **event_args):
    m1 = self.m1.text * pow(10, self.m1_scinot.text)
    m2 = self.m2.text * pow(10, self.m2_scinot.text)
    r = self.r.text * pow(10, self.r_scinot.text)
    g = 6.61 * pow(10, -11)

    gravity = (g *m1 *m2) / (r*r)
    gravity = round(gravity, 3)
    self.result.text = f"Result: {gravity} N"

