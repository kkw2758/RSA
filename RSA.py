import random

def make_primenumber_list(end):#1부터 end까지의 소수를 구해서 구한소수들을 리스트에 넣어서 리턴해주는 함수
	primenumber = [2]
	for i in range(3,end):#소수를 구할 범위를 정하는단계
		j = 0				 #while문 루프가 끝날때마다 j의 값을초기화
		index = i
		while True:
			if i%primenumber[j] == 0:	#i가 나눠진다. => 소수가 아니다. i가 소수 리스트의 원소값에 의해 나눠진다면 for 문의 다음 루프로 간다.
				break
			else:						#i가 나눠지지않는다? 더작은 범위에서 생각이 가능할것이다.
				index = int(i/primenumber[j])+1#index보다 작은 값에서 i를 나눌수있는 값이 없으면 i는 소수이다.
			if primenumber[j] >= index :#index 값보다 더작은 소수가 없다 그러면 추가
				primenumber.append(i)
				break
			else:
				j += 1
	return primenumber
	
	
def gcd(a,b):
	if a < b:		#gcd(a,b)에서 a가 항상 b 보다 크도록 배치해주는 과정
		a,b = b,a
	while b != 0:	#유클리드 호제법을 통해서 a와b의 최대 공약수는 b와 a%b의 최대 공약수와 같다. 는걸이용
		a,b = b, a%b
	return a		#나머지가 0이 되도록 하는수가 a와 b 의 최대공약수가 되므로 그값인 a 를 리턴
	
	
def decrypt(privatekey,ciphertext): #복호화 과정,privatekey는 튜블 형식으로 받음<N,e>
	n, key = privatekey 			#리스트안에 for문 포함하기
	plain = [chr((char ** key) % n) for char in ciphertext] #c^d d가 publickey
	return ''.join(plain)			#리스트를 문자열로 변경해주는 함수 split()함수와 반대 느낌
	
	
def encrypt(publickey, plaintext):	#암호화 과정, publickey이용하고 마찬가지로 튜플형식으로 받음<N,d>
	n,key = publickey
	cipher = [(ord(char)**key) % n  for char in plaintext] #평문에서 문자하나씩 가져와서 가져온 문자의(코드값**e % n)을 계산하여 암호화
	return cipher
	
	
def get_private_key(e, totient): 	#개인키를 얻는과정 <N,d>에서 d 를 얻는 과정이다.
	d = 1
	while (e*d)%totient != 1 or d == e:
		d += 1
	return d

def coprime(totient):		#오일러함수의 결과보다 작고 오일러함수의 결과값이랑 서로소인 숫자들을 모아서 리스트로 리턴해주는 함수.
	coprime_list = []
	for x in range(2,totient):
		if gcd(x,totient) == 1:
			coprime_list.append(x)#totient와 서로소인 값은 coprime_list에 추가한다<coprime = 서로소 라는뜻>
	return coprime_list
		
		
def get_public_key(totient):	#이름그대로 공개키 <N,e>를 얻는과정
	co_list = coprime(totient) 
	return random.choice(co_list)
	
	
m = input("Enter the text to be encrypted:")#평문을 입력받는 과정

prime_number_list = make_primenumber_list(1000)
p = random.choice(prime_number_list)			#prime_number_list라는 소수 리스트에서 소수를 뽑는과정
q = random.choice(prime_number_list)

while True:  #p,q 는 소수이며 서로 다른 수여야 한다.
	if p == q:
		p = random.choice(prime_number_list)
		q = random.choice(prime_number_list)
	else:
		break


print("Two prime numbers(p and q) are:",str(p),"and",str(q))

n = p*q

print("n(p*q)=",str(p),"*",str(q),"=",str(n))

totient = (p-1)*(q-1)
print("(p-1)*(q-1)=",str(totient))

e = get_public_key(totient)
print("Pubic key(n, e):("+str(n)+","+str(e)+")")

d= get_private_key(e,totient)
print("Private key(n,d):("+str(n)+","+str(d)+")")

encrypted_msg = encrypt((n,e),m)#리스트 형태
print('Encrypted Message: ',''.join(list(map(lambda x:str(x),encrypted_msg))))#int값이 멤버인 리스트에서 각멤버를 문자열로 바꾼다음 join()함수를 써서 문자열로 통합하여 출력

print('Decrypted Message:',decrypt((n,d),encrypted_msg))

