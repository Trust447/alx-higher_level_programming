#!/usr/bin/python3
if __name__ == "__main__":
      import sys

      count = len(sys.argv) - 1
      if count == 0:
          sufix = "arguments."
      elif count == 1:
           sufix = "argument:"
      else:
          sufix = "arguments:"
           print("{} {}".format(count, sufix))
           for index, arg in enumerate(sys.argv, start=0):
                if index != 0:
                    print("{}: {}".format(index, arg))
