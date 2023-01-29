# for chip
from textual.widgets import Label
from rich.text import Text, TextType
from textual.app import ComposeResult


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
    
    self.pre = pre or ""
    self.post = post or ""

    self.fg = foreground or "black"
    self.bg = background or "white"

    self.end = ""
    if variant == "color-icon-box":
        self.end = f"[{self.bg} on {variantColor}]{self.icon}[/][{variantColor}]{self.post}"
        self.label = f"{self.label} "
    elif variant == "color-icon":
        self.end = f"[{variantColor} on {self.bg}]{self.icon}[/]{self.post}"
    else:
        self.end = f"{self.icon}{self.post}"

    if shapedBox:
        if variant == "color-icon-box":
            self.end = f"[{self.bg} on {variantColor}]{self.post}[{variantColor} on {self.fg}]{self.end}[/]"
        elif variant == "color-icon":
            self.end = f"[{self.bg} on {variantColor}]{self.post}[/][{variantColor} on {self.bg}]{self.post}[{self.bg} on {self.fg}]{self.end}"
  
  def compose(self) -> ComposeResult:
    yield Label(f"[{self.bg} on {self.fg}]{self.pre}[/][{self.fg} on {self.bg}]{self.label}[/][{self.bg} on {self.fg}]{self.end}[/]")
    