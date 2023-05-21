# Import the redis library
import redis

# Connect to the redis container
r = redis.Redis(host='redis', port=6379, db=0)

# Set a key-value pair
r.set('key', 'value')

# Get the value for a key
value = r.get('key')
print(value)
