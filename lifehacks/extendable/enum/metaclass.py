'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from __future__ import annotations
from itertools import chain
from typing import Generic, Iterable, TypeVar

from lifehacks.extendable.meta import meta
from lifehacks.extendable.enum.exceptions import ENUM_NO_INSTANTIATION


T = TypeVar('T')

################################################################
#######                    metaclass                     #######
################################################################
@meta
class enum(type, Generic[T]):
	''' metaclass for `Enum`\n
		can be used as a `type` for type hinting\n
		e.g.
		```python
		def use_theme(self, theme:enum) -> None:
			self.theme:enum = theme
		```
	'''

	def __new__(cls:type, name:str,
		bases:tuple[type], dictionary:dict
	) -> type:
		created_class = super(cls, cls).__new__(cls, name, bases, dictionary)
		created_class.__init__ = ENUM_NO_INSTANTIATION
		return created_class

	def __str__(cls) -> str:
		# original = repr(cls).strip('<>')
		fields = ', '.join(f'{name}={value}' for name, value in cls)
		return f'<{type(cls).__name__} {cls.__name__}({fields})>'

	def __iter__(cls) -> Iterable[tuple[str, T]]:
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
			rgba(0,0,0) in Palette  # True
			```
		'''
		return obj in [ attr for _, attr in cls ]
