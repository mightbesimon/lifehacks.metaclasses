'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from typing import Any, Generic, Iterator, TypeVar

from .meta import meta
from .exceptions import EnumException


T = TypeVar('T')

################################################################
#######                    metaclass                     #######
################################################################
@meta
class enum(type, Generic[T]):
	'''	metaclass for enum classes
		```python
		@enum
		class BasePalette:
			BLACK = ...
			WHITE = ...

		# extending base palette enum
		class SubPalette(BasePalette):
			RED = ...
			GREEN = ...

		# can be used in type hinting
		def print_colours(palette:enum) -> None:
			for name, value in palette:
				print(name, value)

		print_colours(BasePalette)
		print_colours(SubPalette)
		print(BasePalette.BLACK in SubPalette) # True
		```
	'''

	def __new__(cls:type,
		name:str,
		bases:tuple[type],
		attrs:dict[str, Any],
	) -> type:
		created_class: type = super(enum, cls).__new__(cls, name, bases, attrs)  # type: ignore
		created_class.__init__ = enum.NO_INSTANTIATION
		return created_class

	def __str__(cls) -> str:
		fields = ', '.join(f'{name}={value}' for name, value in cls)
		return f'<{cls.__class__.__name__} {cls.__name__}({fields})>'

	def __iter__(cls) -> Iterator[tuple[str, T]]:
		'''	return all enum items from this enum
			as well as from base enums\n
			e.g.
			```python
			for name, value in Palette:
				template = template.replace(name, str(value))
			```
		'''
		return (
			(name, getattr(cls, name))
			for name in dir(cls)
			if name==name.lstrip('_')
		)

	def __contains__(cls, obj:T) -> bool:
		'''	check if obj is in this enum
			as well as in base enums\n
			e.g.
			```python
			rgba(0,0,0,1) in Palette  # True
			```
		'''
		return obj in [ attr for _, attr in cls ]

	@staticmethod
	def NO_INSTANTIATION(*args:Any, **kwargs:Any):
		raise EnumException('Enum classes cannot be instantiated')
