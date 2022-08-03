'''	Copyright © 2022 mightbesimon.com
	All rights reserved.

	Material belonging to others may have been
	used under Creative Commons Licence or with
	explicit or implicit permission.
'''

################################################################
#######                     exports                      #######
################################################################

from .exceptions import EnumException, ENUM_NO_INSTANTIATION
from .metaclass import enum

__all__ = [enum, EnumException, ENUM_NO_INSTANTIATION]
