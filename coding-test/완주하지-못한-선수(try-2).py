# 해시를 이용한 검색 - 실패
# https://programmers.co.kr/learn/courses/30/lessons/42576#

# 2021.05.07 / 정승균
# 프로그래머스 Level-1 : 완주하지 못한 선수




# 해시 테이블을 위한 클래스 정의
class Hash:
	# 해시 테이블이 담길 리스트
	table = list()
	# 해시함수 사용에 필요한 해시테이블의 크기
	size = 0

	# 해시테이블의 크기를 넘겨받는 생성자
	def __init__( self, size ):
		self.size = size
		for i in range( size ):
			self.table.append( [] )

	# 해시코드 생성 메소드
	def createCode( self, value ):
		# 변환된 해시코드가 저장될 변수
		code = 0
		# 전달받은 문자열을 아스키코드로 변환
		for v in value:
			code += int( ord(v) )
		# 해시테이블의 division 메소드 실행
		code = code % self.size
		return code

	# 해시테이블 삽입 메소드
	def insert( self, value ):
		# 전달받은 value의 해시코드 구하기
		code = self.createCode( value )
		self.table[code].append( value )

	# 해시테이블이 비어있는지 확인하는 메소드
	def isEmpty( self, code ):
		if len( self.table[code] ) == 0:
			return True
		else:
			return False

	# 해시테이블 삭제 메소드
	def delete( self, code, i ):
		del self.table[code][i]

	# 해시테이블 빈 공간 삭제 메소드
	def clear( self ):
		# 반복문을 위한 인덱스 변수
		i = 0
		# 해시테이블 전체를 돌면서 빈공간이 있는지 확인
		while True:
			# i가 현재 해시테이블의 크기보다 커지면 반복문 탈출
			if i >= len(self.table):
				break
			# i번째 값이 비어있으면
			elif self.isEmpty( i ):
				# 빈 공간 삭제
				del self.table[i]
			# i번째 값이 비어있지 않으면
			else:
				# 다음 i번째 값으로 이동
				i += 1

	# 해시테이블 검색 메소드
	def serch( self, key ):
		# 전달받은 key의 해시코드 구하기
		code = self.createCode( key )
		# 해당 해시코드 공간이 비어있지 않으면
		if not self.isEmpty( code ):
			# key값과 동일한 해시코드 내에서 검색
			for i in range( len(self.table[code]) ):
				if key == self.table[code][i]:
					return [code, i]




# main
def solution(participant, completion):
	# participant 리스트의 크기 전달과 함께 해시 객체 생성
	h = Hash( len(participant) )
	# participant 리스트의 값을 하나씩 해시테이블에 삽입
	for p in participant:
		h.insert( p )

	# completion 리스트의 값을 하나씩 가져와 해시테이블에서 검색
	for key in completion:
		code, index = h.serch( key )
		h.delete( code, index )

	# 리스트의 빈 공간 제거
	h.clear()
	# 리스트를 문자열의 형태로 리턴
	return ''.join( h.table[0] )




participant = ["Aimer", "Banana", "Canna", "Dark", "Evan"]
completion = ["Aimer", "Canna", "Dark", "Evan"]

print( solution(participant, completion) )