#!/usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
	from starkware.python.utils import blockify

@atheris.instrument_func
def TestOneInput(data):
	try:
		blockify(data=data, chunk_size=len(data))
	except:
		return

atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
