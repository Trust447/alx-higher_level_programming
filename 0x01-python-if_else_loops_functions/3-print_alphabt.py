#!/usr/bin/python3
for alpha_exm in range(ord('a'), ord('z')):
    if alpha_exm not in [ord('e'), ord('q')]:
        print("{}".format(chr(alpha_exm)), end="")
