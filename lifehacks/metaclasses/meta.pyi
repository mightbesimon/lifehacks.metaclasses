'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

class meta(type):
	'''	metaclass for metaclasses 🍾\n
		what an invention! 🎉\n
		allows subsequent metaclasses to use the decorator
		creation syntax.\n
		When making metaclasses, this syntax super powerful!

		example:
		```python
		@meta
		class enum(type): ...

		@enum	# decorator creation syntax
		class Palette1: ...

		# normal metaclass syntax
		class Palette2(metaclass=enum): ...
		```
	'''
	def __new__(cls, *args:..., **kwargs:...) -> type: ...
	def __init__(self, *args:..., **kwargs:...) -> None: ...
	def __repr__(cls) -> str:
		'''	example:
			```plaintext
			<meta 'meta'>
			<meta 'enum'>
			<enum 'Palette'>
			```
		'''
