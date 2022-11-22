'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from typing import Any


class meta(type):
	'''stub'''
	def __new__(cls, *args:Any) -> type: ...
	def __init__(self, *args:Any) -> None: ...
	def __repr__(cls) -> str: ...
