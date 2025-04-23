def is_valid_mac(mac):
    import re
    pattern = re.compile(r"([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})")
    return pattern.fullmatch(mac) is not None
