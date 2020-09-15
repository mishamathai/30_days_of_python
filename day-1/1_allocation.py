def is_digit(check_input):
    if check_input.isdigit():
        return True
    return False

def main():
	t=input()
	if is_digit(t) == True:
		l = []
		t = int(t)
		nums = [numbers for numbers in range(0,t*2)]
		for i in nums:
			list_vals = input()
			inner_list = list_vals.split()
			for i in inner_list:
				if is_digit(i) == False:
					raise ValueError('improper list values')
			if i%2 == 0:
				if len(inner_list) != 2:
					raise ValueError('more values detected in test case lines') 		
			l.append(inner_list)
		print(l)
		
			

if __name__ == '__main__':
	main()
