'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

from unittest import TestCase, main
from lifehacks.extendable.meta import meta


################################################################
#######                     fixtures                      #######
################################################################


################################################################
#######                      tests                       #######
################################################################
class TestMeta(TestCase):

	def test_meta_decorator(self) -> None:
		@meta
		class enum(type):
			...
		self.assertIsInstance(enum, meta)

	def test_meta_decorator_paran(self) -> None:
		@meta()
		class enum(type):
			...
		self.assertIsInstance(enum, meta)

	def test_meta_metaclass(self) -> None:
		class enum(type, metaclass=meta):
			...
		self.assertIsInstance(enum, meta)


################################################################
#######                 MAIN STARTS HERE                 #######
################################################################
if __name__ == '__main__':
	main()
