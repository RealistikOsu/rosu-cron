from utils import get_user_ids
import globs

TOTAL_SCORES_QUERY = "SELECT (SELECT COUNT(*) FROM scores) + (SELECT COUNT(*) FROM scores_ap) + (SELECT COUNT(*) FROM scores_relax)"

@globs.register_cron()
def cache_redis_stats():
    """Caches all of the main values used for stats in panel."""

    with globs.conn.cursor() as cur:
        cur.execute(TOTAL_SCORES_QUERY)
        total_score, = cur.fetchone()

        total_users = len(get_user_ids(cur))
    
    # Set data in redis.
    globs.redis.set("ripple:registered_users", total_users)
    globs.redis.set("ripple:total_submitted_scores", total_score)
    globs.redis.set("ripple:total_plays", total_score)
