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

	def __new__( cls,
		name:str,
		bases:tuple[type],
		attrs:dict[str, Any],
	) -> type:
		created_class: type = super(enum, cls).__new__(cls, name, bases, attrs)  # type: ignore
		created_class.__init__ = cls.NO_INSTANTIATION
		return created_class

	def __str__(cls) -> str:
		fields = ', '.join(f'{name}={value}' for name, value in cls)
		return f'<{cls.__class__.__name__} {cls.__name__}({fields})>'

	def __iter__(cls) -> Iterator[tuple[str, T]]:
		return (
			(name, getattr(cls, name))
			for name in dir(cls)
			if name==name.lstrip('_')
		)

	def __contains__(cls, obj:T) -> bool:
		return obj in [ attr for _, attr in cls ]

	@staticmethod
	def NO_INSTANTIATION(*args:Any, **kwargs:Any) -> None:
		raise EnumException('\'enum\' classes cannot be instantiated')
