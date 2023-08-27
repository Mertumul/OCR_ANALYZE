import redis
from dynaconf import Dynaconf

settings = Dynaconf(settings_file="settings.toml")

REDIS_HOST = settings.redis.host
REDIS_PORT = int(settings.redis.port)

redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
