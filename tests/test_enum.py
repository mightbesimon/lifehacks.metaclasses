'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from unittest import TestCase, main
from lifehacks.metaclasses import enum, EnumException


################################################################
#######                      tests                       #######
################################################################
class TestEnum(TestCase):

	def test_enum_decorator(self) -> None:
		@enum
		class BaseEnum:
			ONE = 1
			TWO = 2

		self.assertIsInstance(BaseEnum, enum)
		self.assertEqual(type(BaseEnum), enum)
		self.assertEqual(repr(BaseEnum), f'<enum \'{BaseEnum.__module__}.BaseEnum\'>')

	def test_enum_decorator_paran(self) -> None:
		@enum()
		class BaseEnum:
			ONE = 1
			TWO = 2

		self.assertIsInstance(BaseEnum, enum)
		self.assertEqual(type(BaseEnum), enum)
		self.assertEqual(repr(BaseEnum), f'<enum \'{BaseEnum.__module__}.BaseEnum\'>')

	def test_enum_metaclass(self) -> None:
		class BaseEnum(metaclass=enum):
			ONE = 1
			TWO = 2

		self.assertIsInstance(BaseEnum, enum)
		self.assertEqual(type(BaseEnum), enum)
		self.assertEqual(repr(BaseEnum), f'<enum \'{BaseEnum.__module__}.BaseEnum\'>')

	def test_no_instantiation(self) -> None:
		@enum
		class BaseEnum:
			ONE = 1
			TWO = 2

		with self.assertRaises(EnumException):
			_ = BaseEnum()

	def test_iter(self) -> None:
		@enum
		class BaseEnum:
			ONE = 1
			TWO = 2

		self.assertEqual(
			[x for x in BaseEnum],
			sorted(
				[
					('ONE', 1),
					('TWO', 2),
				],
				key=lambda pair: pair[0]
			)
		)

	def test_contains(self) -> None:
		@enum
		class BaseEnum:
			ONE = 1
			TWO = 2

		self.assertFalse(0 in BaseEnum)
		self.assertTrue(1 in BaseEnum)
		self.assertTrue(2 in BaseEnum)


class TestSubEnum(TestCase):

	def test_extend_override(self) -> None:
		@enum
		class BaseEnum:
			ONE = 1
			TWO = 2

		class SubEnum(BaseEnum):
			TWO = 200
			THREE = 3

		self.assertEqual(SubEnum.TWO, 200)
		self.assertFalse(2 in SubEnum)
		self.assertNotIn(('TWO', 2), [x for x in SubEnum])

	def test_extend_iter(self) -> None:
		@enum
		class BaseEnum:
			ONE = 1
			TWO = 2

		class SubEnum(BaseEnum):
			TWO = 200
			THREE = 3

		self.assertEqual(
			[x for x in SubEnum],
			sorted(
				[
					('ONE', 1),
					('TWO', 200),
					('THREE', 3),
				],
				key=lambda pair: pair[0]
			)
		)

	def test_extend_contains(self) -> None:
		@enum
		class BaseEnum:
			ONE = 1
			TWO = 2

		class SubEnum(BaseEnum):
			TWO = 200
			THREE = 3

		self.assertFalse(0 in SubEnum)
		self.assertTrue(1 in SubEnum)
		self.assertFalse(2 in SubEnum)
		self.assertTrue(200 in SubEnum)
		self.assertTrue(3 in SubEnum)


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':
	main()
