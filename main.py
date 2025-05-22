import redis
r = redis.Redis(host='redis', port=6379, db=0) #localhost
r.set('first', 'Hello World!')
print(r.get('first'))