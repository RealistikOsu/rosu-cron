from config import conf
from MySQLdb import connect # I wanna experiment with the low level stuff tho
from redis import Redis

# Create sql conn
conn = connect(
    user= conf.sql_user,
    passwd= conf.sql_password,
    db= conf.sql_password
)

__host, __port = conf.redis_addr.split(":")
redis = Redis(__host, int(__port), conf.redis_pass)
