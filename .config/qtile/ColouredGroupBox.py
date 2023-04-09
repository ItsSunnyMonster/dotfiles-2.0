from qtile_extras import widget
from utils import darken_color

class ColouredGroupBox(widget.GroupBox):
    def draw(self):
        self.drawer.clear(self.background or self.bar.background)

        offset = self.margin_x
        for index, group in enumerate(self.groups):
            highlighted = False

            box_width = self.box_width([group])

            if group.windows:
                text_color = self.colours[index]
            else:
                text_color = darken_color(self.colours[index], 0.5)

            if group.screen:
                if self.bar.screen.group.name == group.name:
                    underline_color = self.colours[index]
                    highlighted = True
                else:
                    underline_color = darken_color(self.colours[index], 0.5)
            elif self.group_has_urgent(group):
                underline_color = self.urgent_underline_color
            else:
                underline_color = None

            self.drawbox(
                offset,
                group.label,
                underline_color,
                text_color,
                highlight_color=self.highlight_color,
                width=box_width,
                rounded=False,
                block=False,
                line=True,
                highlighted=highlighted,
            )
            offset += box_width + self.spacing
        self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.width)

