from ctypes.util import find_library
import ctypes
libc = ctypes.cdll.LoadLibrary(find_library("c"))
libc.printf(b"Hello world!\n")