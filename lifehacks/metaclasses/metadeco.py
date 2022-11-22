'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from functools import wraps
from typing import Any


def metadeco(cls:type) -> type:
	target_new = cls.__new__

	@wraps(target_new)
	def __new__(cls:type, *args:Any) -> type:
		if ( len(args)==3
			and isinstance(args[0], str)
			and isinstance(args[1], tuple)
			and isinstance(args[2], dict)
		):
			# called as metaclass=enum or enum(name, bases, dict)
			name, bases, attrs = args
			return target_new(cls, name, bases, attrs)

		if len(args)==1 and isinstance(args[0], type):
			# called as @enum
			return cls(
				args[0].__name__,
				args[0].__bases__,
				dict(args[0].__dict__),
			)

		if not args:
			# called as @enum()
			return cls

		raise TypeError(
			'no matching use case\n\n'
			'YourClass(metaclass=yourmeta):\n\t...\n\n'
			'@yourmeta\nclass YourClass:\n\t...\n\n'
			'@yourmeta()\nclass YourClass:\n\t...\n\n'
		)

	cls.__new__ = __new__ # type: ignore
	return cls
