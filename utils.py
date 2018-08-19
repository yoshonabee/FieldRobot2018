from argparse import ArgumentParser

def get_args():
	parser = ArgumentParser(prog='python3 fieldRobot.py')

	parser.add_argument('eggs_info_filepath', help='positional argument 1')
	parser.add_argument('-r', '--optional-arg', help='numbers of remain eggs', dest='remain', default=None)

	# parser.print_help()

	return parser.parse_args()