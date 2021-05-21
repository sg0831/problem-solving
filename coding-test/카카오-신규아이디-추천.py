# 2021.03.22 / 정승균
# 카카오 코딩 테스트 - 신규 아이디 추천

def solution(new_id):
	# Step.1 : 소문자 변환
	new_id = new_id.lower()

	# Step.2 : 허락되지 않은 문자 제거
	for ch in new_id:
		if not( ch.isalpha() or ch.isdigit() or ch == "-" or ch == "_" or ch == "."):
			new_id = new_id.replace(ch, "")

	# Step.3 : 연속된 마침표를 하나로 치환
	# find()메소드는 일치하는 값이 없으면 -1을 반환
	while not new_id.find("..") == -1:
		new_id = new_id.replace("..", ".")

	# Step.4 : 처음이나 끝의 마침표 제거
	# 마침표 하나만 남아있으면 마침표를 제거하고 이하 과정 생략
	if new_id == ".":
		new_id = new_id.replace(".", "")
	else:
		# 첫 번째 마침표 확인
		if new_id[0] == ".":
			# 맨 앞의 문자를 제거하기 위한 슬라이싱
			new_id = new_id[1:]
		# 마지막 마침표 확인
		if new_id[-1] == ".":
			# 맨 뒤의 문자를 제거하기 위한 슬라이싱
			new_id = new_id[:-1]

	# Step.5 : 빈 문자열일 경우 "a" 대입
	if len(new_id) == 0:
		new_id = "a"

	# Step.6 : 16자리 이상일 경우 나머지 모두 제거
	if len(new_id) >= 16:
		new_id = new_id[:15]
	# 마지막에 마침표가 있는지 확인
	if new_id[-1] == ".":
		# 맨 뒤의 문자를 제거하기 위한 슬라이싱
		new_id = new_id[:-1]

	# Step.7 : 2자 이하일 경우 3자로 만들기
	while len(new_id) <= 2:
		# 마지막 문자를 맨 뒤에 추가
		new_id += new_id[-1]

	return new_id


# print( solution( input() ) )