from ._anvil_designer import atomic_homeTemplate
from anvil import *
import anvil.server


class atomic_home(atomic_homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def photon_energy_link_click(self, **event_args):
    anvil.open_form("atomic_home.energia_foton")

  def orbit_escape_velocity_link_click(self, **event_args):
    anvil.open_form("predkoscKosmiczna")

  def head_link_click(self, **event_args):
    open_form('home')