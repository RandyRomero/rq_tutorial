import redis
import rq_tutorial_config

r = redis.Redis(host='0.0.0.0', password=rq_tutorial_config.redispass)
print(r.set('foo', 'bar'))
