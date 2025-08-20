import redis

r = redis.Redis(host="localhost", port=6379, db=0)

r.set("name","Riya")
print(r.get("name").decode("utf-8"))