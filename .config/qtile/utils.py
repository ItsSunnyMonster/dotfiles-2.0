import math

def hex2rgb(hex_value: str):
    h = hex_value.strip("#")
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    return rgb


def rgb2hsv(rgb_value: tuple):
    # Normalize R, G, B values
    r, g, b = rgb_value[0] / 255.0, rgb_value[1] / 255.0, rgb_value[2] / 255.0

    # h, s, v = hue, saturation, value
    max_rgb = max(r, g, b)
    min_rgb = min(r, g, b)
    difference = max_rgb-min_rgb

    # if max_rgb and max_rgb are equal then h = 0
    if max_rgb == min_rgb:
        h = 0

    # if max_rgb==r then h is computed as follows
    elif max_rgb == r:
        h = (60 * ((g - b) / difference) + 360) % 360

    # if max_rgb==g then compute h as follows
    elif max_rgb == g:
        h = (60 * ((b - r) / difference) + 120) % 360 
    # if max_rgb=b then compute h
    elif max_rgb == b:
        h = (60 * ((r - g) / difference) + 240) % 360

    # if max_rgb==zero then s=0
    if max_rgb == 0:
        s = 0
    else:
        s = (difference / max_rgb) * 100

    # compute v
    v = max_rgb * 100
    # return rounded values of H, S and V
    return tuple(map(round, (h, s, v)))


def hsv2hex(hsv_value: tuple):
    # h, s, v = hue, saturation, value
    h, s, v = hsv_value[0], hsv_value[1] / 100, hsv_value[2] / 100

    # if s is 0 then h = -1 (undefined)
    if s == 0.0:
        h = -1

    # compute f, i, p, q, t
    f = h / 60.0
    i = math.floor(f)
    p = v * (1 - s)
    q = v * (1 - s * (f - i))
    t = v * (1 - s * (1 - (f - i)))

    # if i is equal to 0
    if i == 0:
        r, g, b = v, t, p

    # if i is equal to 1
    elif i == 1:
        r, g, b = q, v, p

    # if i is equal to 2
    elif i == 2:
        r, g, b = p, v, t

    # if i is equal to 3
    elif i == 3:
        r, g, b = p, q, v

    # if i is equal to 4
    elif i == 4:
        r, g, b = t, p, v

    # if i is equal to 5
    elif i == 5:
        r, g, b = v, p, q

    # convert to int
    r, g, b = int(r * 255), int(g * 255), int(b * 255)

    # return hex value
    return "#%02x%02x%02x" % (r, g, b)


def darken_color(hex_value, amount=0.5):
    hsv = rgb2hsv(hex2rgb(hex_value))
    hsv = tuple([hsv[0], hsv[1] * amount, hsv[2] * amount])
    return hsv2hex(hsv)
