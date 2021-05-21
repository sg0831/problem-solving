# 해시와 딕셔너리 사용
# https://programmers.co.kr/learn/courses/30/lessons/42576#

# 2021.05.14 / 정승균
# 프로그래머스 Level-1 : 완주하지 못한 선수




# 해시 테이블을 위한 클래스 정의
class Hash:
	# 해시테이블의 크기를 넘겨받는 생성자
	def __init__( self, size ):
		# 해시 테이블이 담길 딕셔너리
		self.table = {}
		# 해시코드
		self.code = 0
		# 해시코드의 합 (추후 검색에서 활용)
		self.sum = 0
		# 해시코드가 나올 수 있는 최대 구간을 정해주는 변수
		self.size = size

	# 해시코드 생성 메소드
	def createCode( self, value ):
		# 해시함수의 연산 실행 : (글자수) + (첫글자의 아스키값) + (마지막 글자의 아스키값)
		self.code = len(value) + int( ord(value[0]) ) + int( ord(value[-1]) )
		# 중복없는 해시코드 생성
		self.code = self.code % self.size
		return self.code

	# 해시테이블 삽입 메소드
	def insert( self, value ):
		# 전달받은 value의 해시코드 구하기
		self.code = self.createCode( value )
		# 해시코드값이 키값으로 존재하는지 확인
		if self.code in self.table:
			# 해당 해시코드 슬롯에 value 삽입
			self.table[ self.code ].append( value )
			# 삽입 후 알파벳 순서대로 정렬
			self.table[ self.code ] = sorted(self.table[ self.code ])
		# 해시코드값이 키값으로 존재하지 않으면
		else:
			self.table[ self.code ] = [value]
		# 해시코드의 총합 증가
		self.sum += self.code

	# 해시테이블 삭제 메소드
	def delete( self, value ):
		# 전달받은 value값으로 해시코드 생성
		self.code = self.createCode( value )
		# 해당 해시코드 내에서 value값을 찾아 삭제
		for i in range( len(self.table[ self.code ]) ):
			if value == self.table[ self.code ][i]:
				# 실제 값을 삭제하지 않고 삭제했다는 표시
				self.table[ self.code ][i] = "<delete>"
				# 중복되는 이름을 모두 지우는 걸 방지하기 위해 한 번 삭제 진행 후 반복문 탈출
				break


# main
def solution(participant, completion):
	# participant 리스트의 크기 전달과 함께 participant의 해시 객체 생성
	pHash = Hash( len(participant) )
	# participant 리스트의 값을 하나씩 해시테이블에 삽입
	for p in participant:
		pHash.insert( p )

	# participant 리스트의 크기 전달과 함께 completion의 해시 객체 생성
	cHash = Hash( len(participant) )
	# completion 리스트의 값을 하나씩 해시테이블에 삽입
	for c in completion:
		cHash.insert( c )

	# completion 리스트를 돌면서 해당하는 값을 pHash.table 해시테이블에서 하나씩 제거
	for c in completion:
		pHash.delete( c )

	# completion이 participant보다 1명 적다는 걸 이용해서 정답이 위치한 해시코드 구하기
	answer_code = pHash.sum - cHash.sum

	# 정답 해시코드 내에서 삭제되지 않은 값을 찾아 리턴
	for i in range( len(pHash.table[ answer_code ]) ):
		if pHash.table[ answer_code ][i] != "<delete>":
			return pHash.table[ answer_code ][i]    