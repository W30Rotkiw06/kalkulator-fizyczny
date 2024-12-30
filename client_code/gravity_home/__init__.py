from ._anvil_designer import gravity_homeTemplate
from anvil import *
import anvil.server


class gravity_home(gravity_homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def grav_force_link_click(self, **event_args):
    anvil.open_form('gravity_home.silaGrawitacji')

  def orbit_escape_velocity_link_click(self, **event_args):
    anvil.open_form('gravity_home.predkoscKosmiczna')



  def head_link_click(self, **event_args):
    open_form('home')