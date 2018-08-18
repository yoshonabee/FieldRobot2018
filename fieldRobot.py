import arduino
from egg import *
from utils import *

arg = get_args()

mission_complete = False



while not mission_complete:
	eggs = get_egg_info(arg.egg_info_filepath)
	for i in eggs:
		i.print()
	