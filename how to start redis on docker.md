run redis on  docker:
docker run --name my_redis -p 6379:6379 -d redis --requirepass "yourpassword"

connect from python script:

~~~~
>>> import redis
>>> r = redis.Redis(host='0.0.0.0', port=6379)
>>> r.set('foo', 'bar')
True
>>>
~~~~

