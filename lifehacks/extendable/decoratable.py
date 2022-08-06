'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from functools import wraps
from typing import Any, Callable


def decoratable(
	target_new:Callable[[type, str, tuple[type], dict], type]
) -> Callable[..., type]:
	'''
	'''
	@wraps(target_new)
	def __new__(cls:type, *args:Any) -> type:
		if (len(args)==3
			and isinstance(args[0], str)
			and isinstance(args[1], tuple)
			and isinstance(args[2], dict)
		):
			# called as metaclass=yourmeta or yourmeta(name, bases, dict)
			name, bases, dictionary = args
			return target_new(cls, name, bases, dictionary)

		if len(args)==1 and isinstance(args[0], type):
			# called as @yourmeta
			return cls(
				args[0].__name__,
				args[0].__bases__,
				dict(args[0].__dict__),
			)

		if not args:
			# called as @yourmeta()
			# cls -> yourmeta:meta
			return cls

		raise Exception(
			'no matching use case\n\n'
			'YourClass(metaclass=yourmeta):\n\t...\n\n'
			'@yourmeta\nclass YourClass:\n\t...\n\n'
			'@yourmeta()\nclass YourClass:\n\t...\n\n'
		)

	return __new__
