'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''


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
	def __new__(cls, metaclass=None, *args):
		''' `@yourmeta()`
			-> `@yourmeta`
			-> `metaclass=yourmeta`
			-> `yourmeta(name, bases, dict)`
		'''
		if args:
			# called as metaclass=meta or meta(name, bases, dict)
			return super(meta, cls).__new__(cls, metaclass, *args)

		if metaclass is None:
			# called as @meta()
			return cls

		# called as @meta
		dictionary = dict(metaclass.__dict__)
		dictionary.update(
			__new__=meta.__new__,
			__repr__=meta.__repr__,
		)
		return cls(
			metaclass.__name__,
			metaclass.__bases__,
			dictionary,
		)

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
