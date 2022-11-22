'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from typing import Any, Generic, Iterator, TypeVar


T = TypeVar('T')

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
	def __new__(cls, *args:Any) -> type: ...
	def __init__(self, *args:Any) -> None: ...
	def __repr__(cls) -> str: ...
	def __str__(cls) -> str: ...

	def __iter__(cls) -> Iterator[tuple[str, T]]:
		'''	return all enum items from this enum
			as well as from base enums\n
			e.g.
			```python
			for name, value in Palette:
				template = template.replace(name, str(value))
			```
		'''

	def __contains__(cls, obj:T|Any) -> bool:
		'''	check if obj is in this enum
			as well as in base enums\n
			e.g.
			```python
			rgba(0,0,0,1) in Palette  # True
			```
		'''

	@staticmethod
	def NO_INSTANTIATION(*args:Any, **kwargs:Any) -> None: ...
