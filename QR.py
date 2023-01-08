import pyshorteners
long_url = input("Enter  ")

type_tiny = pyshorteners.Shortener()
Shortener = type_tiny.tinyurl.short(long_url)

print(" link : " + Shortener)

