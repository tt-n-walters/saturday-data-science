import hashlib
import random

previous_transactions = "stuff"
new_bitcoin_for_me = "his"
while True:
    data = previous_transactions + new_bitcoin_for_me + str(random.random())

    hashed = hashlib.md5(data.encode("ascii"))
    digest = hashed.hexdigest()

    print(digest, end="\r")
    if digest[0:6] == "000000":
        break
