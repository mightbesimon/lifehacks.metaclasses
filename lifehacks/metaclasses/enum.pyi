'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from typing import Any, Generic, Iterator, TypeVar


T = TypeVar('T')

class enum(type, Generic[T]):
	'''stub'''
	def __new__(cls, *args:Any) -> type: ...
	def __init__(self, *args:Any) -> None: ...
	def __repr__(cls) -> str: ...
	def __str__(cls) -> str: ...
	def __iter__(cls) -> Iterator[tuple[str, T]]: ...
	def __contains__(cls, obj:T|Any) -> bool: ...

	@staticmethod
	def NO_INSTANTIATION(*args:Any, **kwargs:Any) -> None: ...
