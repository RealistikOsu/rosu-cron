# All of the enums and stuff like that.
class Modes:
    STD   = 0
    TAIKO = 1
    CTB   = 2
    MANIA = 3

    ALL   = (STD, TAIKO, CTB, MANIA)

class CustomModes:
    VN = 0
    RX = 1
    AP = 2

    ALL = (VN, RX, AP)

# Taken from https://github.com/osuripple/ripple-python-common/blob/master/constants/privileges.py
class Privileges:
    USER_PUBLIC = 1
    USER_NORMAL = 2 << 0
    USER_DONOR = 2 << 1
    ADMIN_ACCESS_RAP = 2 << 2
    ADMIN_MANAGE_USERS = 2 << 3
    ADMIN_BAN_USERS = 2 << 4
    ADMIN_SILENCE_USERS = 2 << 5
    ADMIN_WIPE_USERS = 2 << 6
    ADMIN_MANAGE_BEATMAPS = 2 << 7
    ADMIN_MANAGE_SERVERS = 2 << 8
    ADMIN_MANAGE_SETTINGS = 2 << 9
    ADMIN_MANAGE_BETAKEYS = 2 << 10
    ADMIN_MANAGE_REPORTS = 2 << 11
    ADMIN_MANAGE_DOCS = 2 << 12
    ADMIN_MANAGE_BADGES = 2 << 13
    ADMIN_VIEW_RAP_LOGS = 2 << 14
    ADMIN_MANAGE_PRIVILEGES = 2 << 15
    ADMIN_SEND_ALERTS = 2 << 16
    ADMIN_CHAT_MOD = 2 << 17
    ADMIN_KICK_USERS = 2 << 18
    USER_PENDING_VERIFICATION = 2 << 19
    USER_TOURNAMENT_STAFF = 2 << 20