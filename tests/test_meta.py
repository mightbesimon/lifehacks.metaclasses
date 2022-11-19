'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from unittest import TestCase, main
from lifehacks.metaclasses import meta


################################################################
#######                      tests                       #######
################################################################
class TestMeta(TestCase):

	def test_meta_decorator(self) -> None:
		@meta
		class enum(type):
			...

		self.assertIsInstance(enum, meta)
		self.assertEqual(type(enum), meta)
		self.assertEqual(repr(enum), f'<meta \'{enum.__module__}.enum\'>')
		self.assertEqual(repr(meta), f'<meta \'{meta.__module__}.meta\'>')

		@enum
		class Palette:
			...

		self.assertIsInstance(Palette, enum)
		self.assertEqual(type(Palette), enum)
		self.assertEqual(repr(Palette), f'<enum \'{Palette.__module__}.Palette\'>')

	def test_meta_decorator_paran(self) -> None:
		@meta()
		class enum(type):
			...

		self.assertIsInstance(enum, meta)
		self.assertEqual(type(enum), meta)
		self.assertEqual(repr(enum), f'<meta \'{enum.__module__}.enum\'>')
		self.assertEqual(repr(meta), f'<meta \'{meta.__module__}.meta\'>')

		@enum()  # type: ignore
		class Palette:
			...

		self.assertIsInstance(Palette, enum)  # type: ignore
		self.assertEqual(type(Palette), enum)
		self.assertEqual(repr(Palette), f'<enum \'{Palette.__module__}.Palette\'>')

	def test_meta_metaclass(self) -> None:
		class enum(type, metaclass=meta):
			...

		self.assertIsInstance(enum, meta)
		self.assertEqual(type(enum), meta)
		self.assertEqual(repr(enum), f'<meta \'{enum.__module__}.enum\'>')
		self.assertEqual(repr(meta), f'<meta \'{meta.__module__}.meta\'>')

		class Palette(metaclass=enum):
			...

		self.assertIsInstance(Palette, enum)
		self.assertEqual(type(Palette), enum)
		self.assertEqual(repr(Palette), f'<enum \'{Palette.__module__}.Palette\'>')


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':
	main()
