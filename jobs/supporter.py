#Supporter related cron jobs.
import globs
from utils import get_timestamp
from config import conf
from const import Privileges
from logger import info

@globs.register_cron()
def remove_expired_supporters():
    """Removes expired supporter badges and privileges."""

    cur_ts = get_timestamp()

    where_conds = f"WHERE donor_expire < {cur_ts} AND privileges & {Privileges.USER_DONOR}"
    with globs.conn.cursor() as cur:
        cur.execute(
            "SELECT id FROM users " + where_conds
        )

        count_db = [str(uid) for uid, in cur.fetchone()]

        if not count_db: return info("No expired donor tags. Finishing job.")
        
        comma_list = ",".join(count_db)
        # Do most in a single sweep.
        cur.execute(
            f"UPDATE users u SET u.privileges = u.privileges - {Privileges.USER_DONOR},"
            "u.donor_expire = 0, st.show_custom_badge = 0, st.can_custom_badge = 0 "
            "INNER JOIN users_stats st ON u.id = st.id " + where_conds
        )

        # Delete all badges for these users.
        cur.execute(
            f"DELETE FROM user_badges WHERE user IN ({comma_list}) AND "
            f"badge = {conf.sup_badge_id}"
        )

        info(f"Successfully removed {len(count_db)} expired supporter tags + benefits.")
