# if the number of unique characters in a username is odd, then this user is a bot, 
# otherwise this user is a real person
def q1(word):
	uniq = []
	wordlist = list(word)
	for i in wordlist:
		if(i not in uniq):
			uniq.append(i)

	if(len(uniq)%2 != 0):
		return 'BOT'
	return 'DOGE'
if __name__ == '__main__':
    print(q1('muchcoin'))