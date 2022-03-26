import hashlib

message = input()

print(hashlib.sha256(message.encode()).hexdigest())