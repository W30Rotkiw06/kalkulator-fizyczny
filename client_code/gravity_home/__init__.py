from ._anvil_designer import gravity_homeTemplate
from anvil import *
import anvil.server


class gravity_home(gravity_homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def grav_force_link_click(self, **event_args):
    anvil.open_form('silaGrawitacji')

  def orbit_escape_velocity_link_click(self, **event_args):
    anvil.open_form('predkoscKosmiczna')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

