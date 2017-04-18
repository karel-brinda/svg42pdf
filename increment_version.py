#! /usr/bin/env python3

fn="svg42pdf/version.py"

exec(open(fn).read())

numbers=VERSION.split(".")
numbers[-1]=str(int(numbers[-1])+1)

version=".".join(numbers)

with open(fn,"w") as f:
	f.write('VERSION="{}"'.format(version))
