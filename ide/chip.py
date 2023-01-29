# for chip
from textual.widgets import Label, Static
from rich.text import Text, TextType
from textual.app import ComposeResult
from textual.color import Color


class Chip(Label, can_focus=True):
  """simple chips"""
  DEFAULT_CSS = """
  Chip {
    border: none;
    min-width: 0;
    height: 1;
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
    pre: str | None = None,
    post: str | None = None,
    variant: str | None = None,
    variantColor: str | None = None,
    background: str | None = None,
    foreground: str | None = None,
    shapedBox: bool | None = None
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
    
    self.post = post or "░▒▓"
    self.pre = pre or "▓▒░"


    self.end = f"{self.icon}{self.post}"
    
    self.styles.background = Color.parse("pink")
    

  def compose(self) -> ComposeResult:
    yield Label(f"[#1e2030]{self.pre}[/]{self.label}[#1e2030]{self.end}[/]")
    