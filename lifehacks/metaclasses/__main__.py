'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

if __name__ == '__main__':
	print('''
		Copyright © 2022 mightbesimon.com
		All rights reserved.

		Material belonging to others may have been
		used under Creative Commons Licence or with
		explicit or implicit permission.

################################################################
#######              lifehacks.metaclasses               #######
################################################################

usage:
```python
@meta
class YourMetaclass(type): ...

@enum
class PaletteBase:
	BLACK = ...
	WHITE = ...

class SubPalette1(Palette):
	RED = ...

for name, value in SubPalette1:
	print(name, value)
```
''')
