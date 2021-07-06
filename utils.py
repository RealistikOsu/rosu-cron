# Simple ultility functions to carry our repetitive tasks quickly.
from MySQLdb import BaseCursor
import time
import math

def get_countries(cur: BaseCursor) -> list:
    """Gets a list of all countries that have played on the server (2 letter
    codes)."""

    cur.execute("SELECT DISTINCT country FROM users_stats")

    return [country for country, in cur.fetchall()]

def get_user_ids(cur: BaseCursor) -> list:
    """Gets a list of all existing user ids."""

    cur.execute("SELECT id FROM users")
    return [uid for uid, in cur.fetchall()]

def get_timestamp() -> int:
    """Gets the current UNIX timestamp as a full integer."""

    # Several ns faster.
    return math.ceil(time.time())
