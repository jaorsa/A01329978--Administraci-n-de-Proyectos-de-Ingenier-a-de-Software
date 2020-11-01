import redis

r = redis.StrictRedis(
        host='104.198.244.0',
        port=6379, 
        charset = "utf-8",
        decode_responses=True
        )

r.set('ip_address', '0.0.0.0');
print("ip : ", r.get('ip_address'));
