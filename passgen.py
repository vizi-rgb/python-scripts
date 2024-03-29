#! /usr/bin/python
import argparse	
import secrets
import string

tab = ['i','I','l','1','o','O','0']

LOWER = list(filter(lambda a: a not in tab, string.ascii_lowercase))
UPPER = list(filter(lambda a: a not in tab, string.ascii_uppercase))
NUMBERS = list(filter(lambda a: a not in tab, string.digits))
SPECIAL_CHARS = list(string.punctuation)

def check(p):
	i = 0 
	for x in range(len(p)-1):
		if p[i] == p[i+1]:
			return True
		i += 1
	return False

def main():
	parser = argparse.ArgumentParser(prog='passgen', description='HELP')
	parser.add_argument('length', nargs=1, type=int, choices=range(4,31), help='password length')
	parser.add_argument('-s', '--exclude-special', dest='special', action='store_true', help='exclude special characters from the password')
	parser.add_argument('-d', '--exclude-digits', dest='digits', action='store_true', help='exclude digits form the password')
	parser.add_argument('-L', '--exlude-lowercase', dest='lower', action='store_true', help='exclude lowercase characters from the password')
	parser.add_argument('-U', '--exclude-uppercase', dest='upper', action='store_true', help='exclude uppercase characters from the	password')
	parser.add_argument('-i', '--include-simchars', dest='sim_chars', action='store_true', help='include similar looking characters such as i, I, l, 1, o, O, 0')
	parser.add_argument('-1', dest='fchar', action='store_true', help='first char better be a letter')

	args = parser.parse_args()

	alphabet = '' 

	if args.special == False: alphabet += ''.join(SPECIAL_CHARS)
	if args.digits == False: alphabet += ''.join(NUMBERS)
	if args.lower == False: alphabet += ''.join(LOWER)
	if args.upper == False: alphabet += ''.join(UPPER)
	if args.sim_chars == True and args.lower == False and args.upper == False and args.digits == False:
		alphabet += ''.join(tab)

	l = args.length[0] 
	while True:
		final_pass = ''.join(secrets.choice(alphabet) for i in range(l))

		if args.special == False:
			if len([x for x in SPECIAL_CHARS if x in final_pass]) <= 0:
				continue
		if args.digits == False:
			if len([x for x in NUMBERS if x in final_pass]) <= 0:
				continue
		if args.lower == False:
			if len([x for x in LOWER if x in final_pass]) <= 0:
				continue
		if args.upper == False:
			if len([x for x in UPPER if x in final_pass]) <= 0:
				continue 
		if args.fchar == True:
			if final_pass[0] not in LOWER and final_pass[0] not in UPPER:
				continue
		if check(final_pass) == True:
			continue 

		break

	print(final_pass)

if __name__ == '__main__':
	main()