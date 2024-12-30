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



  def head_link_click(self, **event_args):
    open_form('home')

  def wave_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.open_form('atomic_home.dlugosc_fali')
