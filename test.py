#!/usr/bin/env python3
import sys
import clify

@clify.command
def hello(name, lang, *other):
    if clify.is_option_set("z"):
        print("compression flag set")

    print("Hello, ", name, " in", lang)

if __name__ == "__main__":
    clify.dispatch(sys.argv)