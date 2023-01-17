import random
import datetime

def main():
	num_s = "0,1,2,3,4,5,6,7,8,9"
	char_s = "abcdefghijklmnopqrstuvwxyz"
	spec_s = "!#$%&'()*+,-./:;<=>?@[\]_{|}~"
	pswd_list = []
	
	try:
		psw_len = int(input("Jelszó hossza: "))
		num_req = int(input("Számjegyek száma: "))
		spec_req = int(input("Speciális karakterek száma: "))
		char_req = psw_len - num_req - spec_req
		if (num_req < 0) or (spec_req < 0) or (char_req <=0):
			raise AttributeError()
		
		psw_charset(pswd_list, num_s, num_req)
		psw_charset(pswd_list, char_s, char_req, True)
		psw_charset(pswd_list, spec_s, spec_req)
		
		random.shuffle(pswd_list)
		pswd = "".join(pswd_list)
		
		print("A jelszó hossza:", len(pswd), " A jelszó:", pswd)
	except ValueError:
		print("Hibás adatbevitel. Csak számok adhatók meg.")
	except AttributeError:
		print("Hibás adatbevitel. A számjegyek száma és a speciális karakterek száma nem lehet negatív. A jelszó hossza nem lehet kisebb, mint 1. A jelszó hossza nem lehet kisebb, mint a számjegyek számának és a speciális karakterek számának összege.")

def psw_charset(psw, code, req_quantity, cap=False):
	now = datetime.datetime.now()
	random.seed(int(now.strftime("%S")))

	length1=len(code)-1
	for i in range(req_quantity):
		randi = random.randint(0,length1)
		ch = code[randi]
		if cap and (random.randint(0,1) == 1):
			ch=ch.capitalize()
		psw.append(ch)

main()
