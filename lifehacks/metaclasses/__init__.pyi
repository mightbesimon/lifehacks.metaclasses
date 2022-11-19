'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from typing import Any, Generic, Iterator, TypeVar


T = TypeVar('T')

################################################################
#######                   metaclasses                    #######
################################################################
class meta(type):

	def __new__(cls, *args:Any) -> type: ...
	def __init__(self, *args:Any) -> None: ...
	def __repr__(cls) -> str: ...


class enum(type, Generic[T], metaclass=meta):

	def __new__(cls, *args:Any) -> type: ...
	def __init__(self, *args:Any) -> None: ...
	def __repr__(cls) -> str: ...
	def __str__(cls) -> str: ...
	def __iter__(cls) -> Iterator[tuple[str, T]]: ...
	def __contains__(cls, obj:T|Any) -> bool: ...


################################################################
#######                    exceptions                    #######
################################################################
class EnumException(Exception): ...
