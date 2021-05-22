# 딕셔너리만 사용
# https://programmers.co.kr/learn/courses/30/lessons/42576#

# 2021.05.22 / 정승균
# 프로그래머스 Level-1 : 완주하지 못한 선수




def solution(participant, completion):
	# participant 딕셔너리 생성
	p_dic = {}
	# participant 딕셔너리 {'name': count} 형태로 초기화
	for p in participant:
		# 이름의 중복 발생 시
		if p in p_dic:
			# 인원수 증가
			p_dic[p] += 1
		else:
			p_dic[p] = 1

	# completion 딕셔너리 생성
	c_dic = {}
	# completion 딕셔너리 {'name': count} 형태로 초기화
	for c in completion:
		# 이름의 중복 발생 시
		if c in c_dic:
			# 인원수 증가
			c_dic[c] += 1
		else:
			c_dic[c] = 1


	# 전체 선수 리스트를 돌면서 p_dic와 c_dic를 비교
	for name in participant:
		# c_dic에 없는 name이라면
		if not name in c_dic:
			# 정답이므로 리턴
			return name
		# p_dic[name]과 c_dic[name]가 가리키는 선수의 인원수가 다를 경우 정답
		elif p_dic[ name ] != c_dic[ name ]:
			return name