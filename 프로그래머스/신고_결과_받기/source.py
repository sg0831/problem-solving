# 프로그래머스 코딩테스트 연습 - 신고 결과 받기 | 프로그래머스 - Chrome
# https://programmers.co.kr/learn/courses/30/lessons/92334


def insertSetInDict( key, data, targetDict ):
    if key in targetDict:
        targetDict[key].add(data)
    else:
        targetDict[key] = { data }


def setReport( report, reportList, targetList ):
    for reportImpo in report:
        # 스페이스를 기준으로 왼쪽은 reporter(신고자) 오른쪽은 target(신고 당하는 자)
        reporter, target = reportImpo.split(" ")
        insertSetInDict(reporter, target, reportList)
        insertSetInDict(target, reporter, targetList)

def decideReport( targetList, k, resolve ):
    for key in targetList:
        # 신고자의 수(신고 당한 횟수)가 k 이상인지 확인
        if len(targetList[key]) >= k:
            resolve.append( key )

def setEmailCount( id_list, reportList, resolve, answer ):
    for id in id_list:
        answer.append(0)
        if id in reportList:
            for target in resolve:
                if target in reportList[id]:
                    answer[-1] += 1

def solution(id_list, report, k):
    answer = []
    # 신고자들이 누구를 신고했는지 담고 있는 딕셔너리
    reportList = {}
    # 신고 당한 사람들이 누구에게 신고당했는지 담고 있는 딕셔너리
    targetList = {}
    # 최종적으로 신고 처리가 확정된 사람들이 담겨 있는 리스트
    resolve = []

    setReport(report, reportList, targetList)
    decideReport(targetList, k, resolve)
    setEmailCount(id_list, reportList, resolve, answer)

    return answer



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
solution(id_list, report, k)