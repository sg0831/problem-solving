# 프로그래머스 - 폰켓몬
# 작성자 : 정승균

def solution( nums ):
	# 선택 가능한 최대 폰켓몬 수
	limit = len(nums) // 2
	# 선택 가능한 폰켓몬의 종류 리스트
	type = []

	# nums에서 선택 가능한 폰켓몬의 종류 모두 구하기
	for i in nums:
		# 불필요한 반복 방지 : 이미 선택 가능한 폰켓몬의 최대 종류 수를 모두 구했다면, 이하 과정 생략
		if len(type) == limit:
			break
		# type리스트 안에 i값이 가 존재하지 않다면, type리스트에 i 추가
		if not i in type:
			type.append( i )

	# 선택 가능한 최대 폰켓몬의 종류 수 리턴
	return len(type)    