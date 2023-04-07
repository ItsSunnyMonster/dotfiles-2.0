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
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration, PowerLineDecoration

import os
import subprocess

mod = "mod4"
terminal = guess_terminal()

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
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons"), desc="Spawn an application using rofi"),
    Key([mod, "shift"], "r", lazy.spawn("rofi -show run"), desc="Spawn a command using rofi"),
    Key([mod], "Tab", lazy.spawn("rofi -show window -show-icons"), desc="Window menu with rofi"),
    Key([mod], "x", lazy.spawn("rofi -show power-menu -modi power-menu:~/.config/rofi/rofi-power-menu"), desc="Power menu with rofi"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Flameshot"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%"), desc="Increase the brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc="Decrease the brightness"),  
    Key([mod, "shift"], "k", lazy.spawn("dunstctl history-pop"), desc="Pop the last notification"),
    Key([mod, "shift"], "j", lazy.spawn("dunstctl close"), desc="Close the last notification"),
    Key([mod, "shift"], "d", lazy.spawn("dunstctl close-all"), desc="Close all notifications"),
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
        Group(""),
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

colors = {
        "black":            "#000000",
        "black_bright":     "#5c6069",
        "black_semibright": "#1d2230",
        "red":              "#fe1f56",
        "red_bright":       "#fd2b72",
        "green":            "#78db88",
        "green_bright":     "#93fd92",
        "yellow":           "#fde063",
        "yellow_bright":    "#fefe6a",
        "blue":             "#24e0fe",
        "blue_bright":      "#73fefb",
        "magenta":          "#d5a3e7",
        "magenta_bright":   "#ecbaf8",
        "cyan":             "#48ccbe",
        "cyan_bright":      "#5cfae3",
        "white":            "#e3e4e0",
        "white_bright":     "#fdfdfd"
}

layouts = [
    layout.MonadTall(margin=10, border_focus=colors["green_bright"], border_normal=colors["black"], border_width=3),
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(margin=10),
    layout.Floating(border_focus=colors["blue_bright"], border_width=3),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="mononoki Nerd Font",
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def open_wifi_menu():
    home = os.path.expanduser('~/.config/rofi/rofi-wifi-menu.sh')
    subprocess.run([home])

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
                    foreground="#090c0c",
                    background="#a3aed2", 
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun -show-icons")},
                    decorations=[
                        RectDecoration(radius=10, use_widget_background=True, filled=True, group=True)
                    ],
                ),
                widget.TextBox(
                    text=" |",
                    fontsize=20,
                    foreground=colors["black_bright"],
                    background=colors["black_semibright"]
                ),
                widget.GroupBox(
                    active=colors["green"], inactive=colors["white"], urgent_text=colors["red_bright"], 
                    highlight_method="line", 
                    rounded=True, 
                    padding_x=5, 
                    margin_x=2, margin_y=4, 
                    urgent_alert_method="text",
                    this_current_screen_border=colors["white"],
                    other_current_screen_border=colors["green"],
                    disable_drag=True,
                    fontsize=30,
                    borderwidth=2,
                    background=colors["black_semibright"],
                    highlight_color="#111725",
                    font="mononoki Nerd Font Mono"
                ),
                widget.TextBox(
                    text="|",
                    fontsize=20,
                    foreground=colors["black_bright"],
                    background=colors["black_semibright"]
                ),
                widget.Backlight(
                    backlight_name="amdgpu_bl0",
                    change_command="brightnessctl set {0}%",
                    foreground=colors["black_semibright"],
                    background=colors["red_bright"],
                    fmt="  {}",
                    decorations=[
                        RectDecoration(radius=10, use_widget_background=True, filled=True, group=True)
                    ],
                ),
                widget.PulseVolume(
                    fmt="墳  {}",
                    foreground=colors["black_semibright"],
                    background=colors["cyan_bright"],
                    update_interval=0.1,
                    decorations=[
                        RectDecoration(radius=10, use_widget_background=True, filled=True, group=True)
                    ],
                ),
                widget.Spacer(),
                widget.WindowName(font="JetBrains Mono Nerd Font"),
                #widget.Chord(
                #    chords_colors={
                #        "launch": ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),
                widget.TextBox(
                    text="",
                    fontsize=34,
                    foreground=colors["black_semibright"],
                    padding=-1
                ),
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
                # widget.Sep(
                #     linewidth=0,
                #     background=colors["black_semibright"],
                #     padding=10
                # ),
                widget.Sep(
                    linewidth=0,
                    background=colors["black_semibright"],
                    padding=10
                ),
                widget.Net(
                    background=colors["black_semibright"],
                    foreground=colors["green_bright"],
                    interface="wlp1s0",
                    format = '↓ {down} ↑ {up}',
                    decorations = [
                        BorderDecoration(
                            colour=colors["green_bright"],
                            border_width=[0, 0, 2, 0],
                        ),
                    ],
                ),
                widget.Sep(
                    linewidth=0,
                    background=colors["black_semibright"],
                    padding=10
                ),
                widget.Battery(
                    charge_char="", 
                    discharge_char="", 
                    empty_char="",
                    full_char="", 
                    fontsize=17,
                    foreground=colors["yellow_bright"],
                    format="{char} {percent:2.0%} {hour:d}:{min:02d}",
                    background=colors["black_semibright"],
                    update_interval=1,
                    show_short_text=False,
                    decorations = [
                        BorderDecoration(
                            colour=colors["yellow_bright"],
                            border_width=[0, 0, 2, 0],
                        ),
                    ],
                ),
                widget.Sep(
                    linewidth=0,
                    background=colors["black_semibright"],
                    padding=10
                ),
                #widget.CurrentLayoutIcon(scale=0.5,background=colors["black_semibright"], foreground=colors["yellow_bright"]),
                widget.CurrentLayout(
                    background=colors["black_semibright"], 
                    foreground=colors["blue_bright"], 
                    fmt="𧻓  {}",
                    decorations = [
                        BorderDecoration(
                            colour=colors["blue_bright"],
                            border_width=[0, 0, 2, 0],
                        ),
                    ],
                ),
                widget.Sep(
                    linewidth=0,
                    background=colors["black_semibright"],
                    padding=10
                ),
                widget.CheckUpdates(
                    no_update_string=" No updates", 
                    display_format="  Updates: {updates}",
                    foreground=colors["green_bright"], 
                    background=colors["black_semibright"], 
                    colour_have_updates=colors["green_bright"], 
                    colour_no_updates=colors["green_bright"],
                    execute="alacritty -e yay -Syu",
                    decorations = [
                        BorderDecoration(
                            colour=colors["green_bright"],
                            border_width=[0, 0, 2, 0],
                        ),
                    ],
                ),
                widget.Sep(
                    linewidth=0,
                    background=colors["black_semibright"],
                    padding=10
                ),
                widget.Clock(
                    format="  %m-%d %I:%M %p", 
                    background=colors["black_semibright"], 
                    foreground=colors["red_bright"],
                    decorations = [
                        BorderDecoration(
                            colour=colors["red_bright"],
                            border_width=[0, 0, 2, 0],
                        ),
                    ],
                ),
                widget.TextBox(
                    text="|",
                    fontsize=20,
                    foreground=colors["black_bright"],
                    background=colors["black_semibright"]
                ),
                widget.Systray(background=colors["black_semibright"]), 
                widget.Sep(
                    linewidth=0,
                    background=colors["black_semibright"],
                    padding=5
                ),
                widget.TextBox(
                    text="",
                    fontsize=33,
                    foreground="#212736",
                    background="#1d2230",
                    padding=-1
                ),
                widget.TextBox(
                    text="",
                    fontsize=34,
                    foreground="#394260",
                    background="#212736",
                    padding=-1
                ),
                widget.TextBox(
                    text="",
                    fontsize=34,
                    foreground="#d74747",
                    background="#394260",
                    padding=-1
                ),
                widget.TextBox(
                    text=" ",
                    foreground=colors["white_bright"],
                    background="#d74747",
                    padding=5,
                    fontsize=20, font="mononoki Nerd Font",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show power-menu -modi power-menu:~/.config/rofi/rofi-power-menu")}
                ),        
                widget.Sep(
                    linewidth=0,
                    background="#a3aed2",
                    padding=13
                ),             
                widget.Sep(
                    linewidth=0,
                    background="#7b839e",
                    padding=13
                ),
                widget.Sep(
                    linewidth=0,
                    background="#525769",
                    padding=13
                ),
                widget.Sep(
                    linewidth=0,
                    background="#292c35",
                    padding=13
                ),
            ],
            30,
            background=colors["black_semibright"],
            margin=[10,10,0,10],
            border_width=7,  # Draw top and bottom borders
            border_color=colors["black_semibright"]  # Borders are magenta
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
    border_focus=colors["blue_bright"],
    border_normal=colors["black"],
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


@hook.subscribe.client_focus
def handle_client_focus(window):
    if window.floating:
        window.cmd_bring_to_front()
