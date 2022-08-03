'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from typing import Any, Callable


def decoratable(
	f:Callable[[type, str, tuple[type], dict], meta]
) -> Callable[..., meta]:
	'''
	'''
	def __new__(cls:type,
		*args:Any
	) -> type:
		if (len(args)==3
			and isinstance(args[0], str)
			and isinstance(args[1], tuple)
			and isinstance(args[2], dict)
		):
			# called as metaclass=yourmeta or yourmeta(name, bases, dict)
			name, bases, dictionary = args
			return f(cls, name, bases, dictionary)

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


class meta(type):
	''' metaclass for metaclasses 🍾\n
		what an invention! 🎉\n
		allows subsequent metaclasses to use the decorator
		creation syntax.\n
		When making metaclasses, this syntax super powerful!

		example:
		```python
		@meta
		class enum(type):
			...

		@enum	# <- decorator creation syntax
		class Palette1:
			...

		# normal metaclass syntax
		class Palette2(metaclass=enum):
			...
		```
	'''
	@decoratable
	def __new__(cls:type,
		name:str,
		bases:tuple[type],
		dictionary:dict
	) -> type:
		created_metaclass = super(meta, cls).__new__(cls, name, bases, dictionary)
		created_metaclass.__repr__ = meta.__repr__
		created_metaclass.__new__ = decoratable(created_metaclass.__new__)
		return created_metaclass

	def __repr__(cls) -> str:
		'''	example:
			```plaintext
			<meta 'meta'>
			<meta 'enum'>
			<enum 'Palette'>
			```
		'''
		return f'<{type(cls).__name__} \'{cls.__module__}.{cls.__name__}\'>'


# self-decorate meta metaclass
meta = meta(meta)
