from textual.app import App, ComposeResult
from textual import events
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Welcome, Button, Tree, Label


# for chip
from textual.widgets import Label
from rich.text import Text, TextType

class Chip(Label, can_focus=True):
  """simple chips"""
  DEFAULT_CSS = """
  Chip {
    border: none;
    min-width: 0;
    height: 1;
    background: transparent;
  }
  """
  
  def __init__(
    self, 
    label: TextType | None = None,
    icon: TextType | None = None,
    *,
    name: str | None = None,
    id: str | None = None,
    classes: str | None = None,
    pre: str | "",
    post: str | ""
  ):
    super().__init__(name=name, id=id, classes=classes)
    
    if label is None:
      label = self.css_identifier_styled
    
    self.label = label
    
    if icon is None:
      icon = ""
    else:
      icon = f" {icon}"
      
    self.icon = icon
    
    self.pre = pre
    self.post = post
  
  
  def compose(self) -> ComposeResult:
    yield Label(f" {self.pre}[reverse] {self.label}{self.icon}[/]{self.post} ")
    

# =========================

class Ide(App):
  CSS_PATH = "styles/base.tss"  
  
  def compose(self) -> ComposeResult:
    files = Button(label="󰈢", id="action__files", classes="selected")
    projects = Button(label="", id="action__projects")
    dashboard = Button(label="󰕮", id="action__dashboard")
    debug = Button(label="", id="action__debug")
    sourcecontrol = Button(label="", id="action__sourcecontrol")
    extensions = Button(label="", id="action__extensions")
    yield Vertical(      
      files,
      projects,
      dashboard,
      debug,
      sourcecontrol,
      extensions

    ,id="actionbar", classes="box")
    
    tree = Tree("dune", id="ldock", classes="box")
    tree.root.expand()
    characters = tree.root.add("Characters", expand=True)
    characters.add_leaf("Paul")
    characters.add_leaf("Jessica")
    characters.add_leaf("Chani")
    yield tree
    
    chip = Horizontal(
      Chip("test 1", icon=""),
      Chip("test 2", icon=""), 
      Chip("test 3"), 
    id="contentpane", classes="box")
    
    yield chip
    
    yield Static("statusbar", id="statusbar", classes="box")

  def on_button_pressed(self, event: Button.Pressed) -> None:
    # if it's an actionbar button
    if event.button.id and event.button.id.startswith("action__"):
      dock = self.query_one("#ldock")
      
      # hiding
      if "selected" in event.button.classes:
        dock.add_class("hidden")
        event.button.remove_class("selected")
        return 
      else:
        selectedExists = self.query("#actionbar Button.selected")
        if selectedExists is not None:
          selectedExists.remove_class("selected")
        dock.add_class("hidden")
        event.button.add_class("selected")
        
      # set dock content
      
      # open files
      if event.button.id == "action__files":
        dock.remove_class("hidden")
    
    
  
if __name__ == "__main__":
  app = Ide()
  app.run()