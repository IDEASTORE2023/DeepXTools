from ctypes import POINTER

from ..wintypes import VARIANT, dll_import


@dll_import('OleAut32')
def VariantInit( pvarg : POINTER(VARIANT) ) -> None: ...
