#!/bin/sh
picom --experimental-backend &
nitrogen --restore &
xsetroot -cursor_name left_ptr &
xrdb -merge ~/.Xresources &
/usr/bin/pipewire &
/usr/bin/pipewire-pulse &
/usr/bin/pipewire-media-session &
discord &
volumeicon &
nm-applet &
xinput --set-prop 'pointer:''2.4G Mouse' 'libinput Accel Profile Enabled' 0, 1 &
xinput --set-prop 'pointer:''2.4G Mouse' 'libinput Accel Speed' 1 &
xinput --set-prop 'pointer:''ELAN2203:00 04F3:309A Touchpad' 'libinput Accel Speed' 1 &
xinput --set-prop 'pointer:''ELAN2203:00 04F3:309A Touchpad' 'libinput Tapping Enabled' 1 &
xinput --set-prop 'pointer:''ELAN2203:00 04F3:309A Touchpad' 'libinput Accel Profile Enabled' 0, 1 &
xinput --set-prop 'pointer:''ELAN2203:00 04F3:309A Touchpad' 'libinput Natural Scrolling Enabled' 1 &
flameshot &
dunst &
fcitx &
redshift-gtk -l $LATLONG -t 6500:3600 &
setxkbmap -option compose:ralt &
