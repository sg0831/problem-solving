# 해시를 이용한 검색 - 실패
# https://programmers.co.kr/learn/courses/30/lessons/42576#

# 2021.05.07 / 정승균
# 프로그래머스 Level-1 : 완주하지 못한 선수




# main
def solution(participant, completion):
	for c in completion:
		for i in len(participant):
			if c == participant[i]:
				del participant[i]
				i -= 1