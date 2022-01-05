def gcd(x,y):
	if x < y:
		return gcd(y,x)
	while y != 0:
		x,y = y,x%y
	return x

class Customerror(Exception):
	def __init__(self,message="Invalid data"):
		self.message = message
		super().__init__(self.message)

def rsa():
	try:
		p = int(input("enter the prime number p: "))
		q = int(input("enter the prime number q: "))
		if(gcd(p,q) != 1):
			raise Customerror(message="gcd of p,q is not 1")
			
		n = p * q
		number = int(input("enter the value to be encrypted or decrypted: "))
		if number>n:
			raise Customerror("Message data is greater than N")
		phi = (p-1)*(q-1)
		e = int(input("enter the value of e: "))
		if(gcd(phi,e) != 1 and e > 1 and e < phi):
			raise Customerror("Invalid value of e")
		d = int(input("enter the value of d: "))
		if(gcd(phi,d) != 1 and d > 1 and d < phi):
			raise Customerror("Invalid value of d")
		#(M  ** e )mod n
		encrypted = (number ** e) % n
		decrypted = (encrypted ** d) % n
		print("The encrypted message is ",encrypted)
		print("The decrypted message is ",decrypted)
	except ValueError:
		print('Non-numeric data entered.')
	except KeyboardInterrupt:
		print('Program stopped by user.')

if __name__ == '__main__':
	rsa()
