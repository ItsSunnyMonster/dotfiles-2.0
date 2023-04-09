# qtile/config.py
# This config file was based on the default config.py
# https://github.com/qtile/qtile/blob/master/libqtile/resources/default_config.py
#  ________  _____ ______      
# |\   ____\|\   _ \  _   \    
# \ \  \___|\ \  \\\__\ \  \   
#  \ \_____  \ \  \\|__| \  \  
#   \|____|\  \ \  \    \ \  \ 
#     ____\_\  \ \__\    \ \__\
#    |\_________\|__|     \|__|
#    \|_________|              

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration

import os
import subprocess

from ColouredGroupBox import *

mod = "mod4"
terminal = guess_terminal()

def spawn_launcher(_):
    subprocess.run(os.path.expanduser("~/.config/rofi/bin/launcher"))
    
def spawn_powermenu(_):
    subprocess.run(os.path.expanduser("~/.config/rofi/bin/powermenu"))

keys = [
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    # toggle between windows with 'alt+tab'
    Key(["mod1","shift"], "Tab", lazy.group.prev_window()),
    Key(["mod1"], "Tab", lazy.group.next_window()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod, "shift"], "n", lazy.layout.reset()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.function(spawn_launcher), desc="Spawn an application using rofi"),
    Key([mod, "shift"], "r", lazy.spawn("~/.config/rofi/bin/launcher"), desc="Spawn a command using rofi"),
    Key([mod], "Tab", lazy.spawn("rofi -show window -show-icons"), desc="Window menu with rofi"),
    Key([mod], "x", lazy.function(spawn_powermenu), desc="Power menu with rofi"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Flameshot"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Increase the brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Decrease the brightness"),  
    Key([mod, "shift"], "k", lazy.spawn("dunstctl history-pop"), desc="Pop the last notification"),
    Key([mod, "shift"], "j", lazy.spawn("dunstctl close"), desc="Close the last notification"),
    Key([mod, "shift"], "d", lazy.spawn("dunstctl close-all"), desc="Close all notifications"),
    Key([mod, "shift"], "t", lazy.hide_show_bar(), desc="Toggle the top bar"),
]

groups = [
        Group(""),
        Group("󰲋"),
        Group("󰌀"),
        Group("󰙯"),
        Group("󰉋"),
        Group("󰍳"),
        Group("󰈙"),
        Group(""),
        Group(""),
]

for i in range(len(groups)):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                str(i+1),
                lazy.group[groups[i].name].toscreen(),
                desc="Switch to group {}".format(groups[i].name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(i+1),
                lazy.window.togroup(groups[i].name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(groups[i].name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

colours = {
    "rosewater":    "#f5e0dc",
    "flamingo":     "#f2cdcd",
    "pink":         "#f5c2c7",
    "mauve":        "#cba6f7",
    "red":          "#f38ba8",
    "maroon":       "#eba0ac",
    "peach":        "#fab387",
    "yellow":       "#f9e2af",
    "green":        "#a6e3a1",
    "teal":         "#94e2d5",
    "sky":          "#89dceb",
    "sapphire":     "#74c7ec",
    "blue":         "#89b4fa",
    "lavender":     "#b4befe",
    "text":         "#cdd6f4",
    "subtext1":     "#bac2de",
    "subtext0":     "#a6adc8",
    "overlay2":     "#9399b2",
    "overlay1":     "#7f849c",
    "overlay0":     "#6c7086",
    "surface2":     "#585b70",
    "surface1":     "#45475a",
    "surface0":     "#313244",
    "base":         "#1e1e2e",
    "mantle":       "#181825",
    "crust":        "#11111b"
}

layouts = [
    layout.MonadTall(margin=10, border_focus=colours["sapphire"], border_normal=colours["base"], border_width=3, new_client_position="top"),
    layout.MonadWide(margin=10, border_focus=colours["sapphire"], border_normal=colours["base"], border_width=3),
    layout.Max(margin=10),
    layout.Floating(border_focus=colours["yellow"], border_width=3),
]

widget_defaults = dict(
    font="mononoki Nerd Font",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def separator():
    return widget.TextBox(
        text="|",
        fontsize=20,
        foreground=colours["overlay0"],
    )
    
        
def box_decoration():
    return RectDecoration(radius=14, use_widget_background=True, filled=True, group=True)
    
def powerline_decoration():
    return PowerLineDecoration(path="arrow_right")
        
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.TextBox(
                    text="", 
                    fontsize=30, 
                    padding=20, 
                    font="mononoki Nerd Font Mono", 
                    foreground=colours["base"],
                    background=colours["blue"], 
                    mouse_callbacks={"Button1": lazy.function(spawn_launcher)},
                    decorations=[box_decoration()]
                ),
                widget.Spacer(length=10),
                separator(),
                ColouredGroupBox(
                    urgent_underline_color=colours["red"], 
                    colours=[
                        colours["lavender"], colours["peach"], colours["blue"], 
                        colours["mauve"], colours["yellow"], colours["green"],
                        colours["sapphire"], colours["red"], colours["sky"]
                    ],
                    padding_x=5, 
                    margin_x=2, margin_y=4, 
                    disable_drag=True,
                    fontsize=30,
                    borderwidth=2,
                    highlight_color=colours["crust"],
                    font="mononoki Nerd Font Mono"
                ),
                separator(),
                widget.Spacer(length=10),
                widget.Backlight(
                    backlight_name="amdgpu_bl0",
                    change_command="brightnessctl set {0}%",
                    foreground=colours["base"],
                    background=colours["rosewater"],
                    fmt="  {}",
                    padding=10,
                    decorations=[box_decoration(), powerline_decoration()]
                ),
                widget.PulseVolume(
                    fmt="墳  {}",
                    foreground=colours["base"],
                    background=colours["pink"],
                    update_interval=0.1,
                    padding=10,
                    decorations=[box_decoration(), powerline_decoration()]
                ),
                widget.Battery(
                    charge_char="", 
                    discharge_char="", 
                    empty_char="",
                    full_char="", 
                    fontsize=17,
                    foreground=colours["base"],
                    format="{char} {percent:2.0%}",
                    background=colours["red"],
                    update_interval=1,
                    show_short_text=False,
                    padding=10,
                    decorations = [box_decoration()],
                ),
                widget.Spacer(),
                widget.WindowName(font="JetBrains Mono Nerd Font", width=450, scroll=True, scroll_interval=0.02, scroll_step=1),
                widget.Spacer(),
                # widget.Bluetooth(
                #     hci="/dev_04_52_C7_83_60_BD",
                #     fmt=" {}",
                #     background=colors["black_semibright"],
                #     foreground=colors["green_bright"],
                #     decorations = [
                #         BorderDecoration(
                #             colour=colors["green_bright"],
                #             border_width=[0, 0, 2, 0],
                #         ),
                #     ],
                #     mouse_callbacks={"Button1": lazy.spawn("alacritty -e bluetoothctl")},
                # ),
                #widget.CurrentLayoutIcon(scale=0.5,background=colors["black_semibright"], foreground=colors["yellow_bright"]),
                widget.CurrentLayout(
                    background=colours["green"], 
                    foreground=colours["base"], 
                    fmt="𧻓  {}",
                    padding=10,
                    decorations = [box_decoration(), powerline_decoration()],
                ),
                widget.CheckUpdates(
                    no_update_string=" No updates", 
                    display_format="  Updates: {updates}",
                    foreground=colours["base"], 
                    background=colours["yellow"], 
                    colour_have_updates=colours["base"], 
                    colour_no_updates=colours["base"],
                    execute="alacritty -e yay -Syu",
                    padding=10,
                    decorations = [box_decoration(), powerline_decoration()],
                ),
                widget.Clock(
                    format="  %m-%d %I:%M %p", 
                    background=colours["teal"], 
                    foreground=colours["base"],
                    padding=10,
                    decorations = [box_decoration()],
                ),
                widget.Spacer(length=5),
                separator(),
                widget.Systray(background=colours["base"]),
                separator(),
                widget.Spacer(length=5),
                widget.TextBox(
                    text="",
                    foreground=colours["base"],
                    background=colours["red"],
                    padding=20,
                    fontsize=30, font="mononoki Nerd Font Mono",
                    decorations = [box_decoration()],
                    mouse_callbacks={"Button1": lazy.function(spawn_powermenu)}
                ),  
                widget.Spacer(length=10)    
            ],
            30,
            background=colours["base"],
            margin=[10,10,0,10],
            border_width=7,  # Draw top and bottom borders
            border_color=colours["base"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="pinentry-gtk-2"),
        Match(wm_class="Unity"),
    ],
    border_focus=colours["yellow"],
    border_normal=colours["base"],
    border_width=3,
)
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

### Autostart
@hook.subscribe.startup_once
def autostart_once():
    command = os.path.expanduser('~/.config/qtile/autostart_once.fish')
    cwd = os.path.expanduser('~/.config/qtile/')
    subprocess.run([command], cwd=cwd)
