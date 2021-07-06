# Simple ultility functions to carry our repetitive tasks quickly.
from MySQLdb import BaseCursor

def get_countries(cur: BaseCursor) -> list:
    """Gets a list of all countries that have played on the server (2 letter
    codes)."""

    cur.execute("SELECT DISTINCT country FROM users_stats")

    return [country[0] for country in cur.fetchall()]
