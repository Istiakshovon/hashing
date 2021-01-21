import hashlib

str2hash = "Hash it"

print("MD5 : "+hashlib.md5(str2hash.encode()).hexdigest())
print("SHA1 : "+hashlib.sha1(str2hash.encode()).hexdigest())
print("SHA256 : "+hashlib.sha256(str2hash.encode()).hexdigest())
print("SHA224 : "+hashlib.sha224(str2hash.encode()).hexdigest())
print("SHA384 : "+hashlib.sha384(str2hash.encode()).hexdigest())
print("SHA512 : "+hashlib.sha512(str2hash.encode()).hexdigest())