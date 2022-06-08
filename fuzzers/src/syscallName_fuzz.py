#!/usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
	from starkware.cairo.common.structs import CairoStructFactory, CairoStructProxy
	from starkware.starknet.core.os.os_program import get_os_program

def get_selector(syscall_name: str):
	os_progoram = get_os_program()
	return os_program.get_const(name=f"starkware.starknet.common.syscalls.{syscall_name.upper()}_SELECTOR",full_name_lookup=True)

def TestOneInput(data):
	try:
		get_selector(str(data))
	except:
		return

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
