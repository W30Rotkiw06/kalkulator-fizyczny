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


