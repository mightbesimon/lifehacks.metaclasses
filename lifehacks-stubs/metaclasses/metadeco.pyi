'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

def metadeco(cls:type) -> type:
	'''	make metaclass decoratable
		```python
		class Palette(metaclass=enum): ...
		# without

		@enum	# clean syntax, readable
		class Palette: ...
		```
	'''
