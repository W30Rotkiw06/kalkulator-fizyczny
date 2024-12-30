from ._anvil_designer import homeTemplate
from anvil import *
import anvil.server


class home(homeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.


  def link_1_click(self, **event_args):
    open_form('gravity_home')

  def atomic_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("atomic_home")


