# 해시함수 충돌을 고민하느라 잠시 작업 중지
# https://programmers.co.kr/learn/courses/30/lessons/42578?language=go

# 2021.05.23 / 정승균
# 프로그래머스 - 위장



class Node:
	def __init__( self, data ):
		# 노드가 저장할 데이터
		self.data = data
		# 다음 노드 객체가 담김
		self.next = None
class LinkedList:
	def __init__( self ):
		# 첫 번째 노드 객체가 담김
		self.head = None
		# 모든 노드의 개수
		self.size = 0

	def insertNode( self, data ):
		# Node객체 생성
		self.newNode = Node( data )
		self.newNode.next = self.head
		self.head = self.newNode
		self.size += 1

	# 테스트 출력용 메소드
	def display( self ):
		print_node = self.head
		for i in range( self.size ):
			print( "{}: {}".format(i, print_node.data) )
			print_node = print_node.next


# 해시함수
def createHashCode( size, value ):
	return (len(value) + int(ord( value[0] )) + int(ord( value[-1] ))) % size
# 미완성
def fillAnswer( hashTable, size, type, answer ):
	# 이 함수에서 사용할 임시 리스트
	tempList = None
	# 전달받은 answer 리스트가 비어있지 않으면
	if len(answer) != 0:
		tempList = answer[-1]
	# type를 하나씩 돌면서 정답이 될 수 있는 모든 경우를 탐색
	for t in type:
		hashCode = createHashCode( size, t )
		tempList.append( hashTable[ hashCode ].head )

def solution( clothes ):
	# 옷의 종류
	type = []
	# clothes의 크기
	size = len(clothes)
	# 연결리스트를 담을 해시테이블
	hashTable = []
	# 해시테이블 초기화
	for i in range( len(clothes) ):
		hashTable.append( None )

	# 연결리스트에 data넣기
	for data in clothes:
		# data의 해시코드 생성
		hashCode = createHashCode( size, data[1] )
		# 해시코드 공간이 비었으면 새 연결리스트 생성
		if hashTable[ hashCode ] == None:
			hashTable[ hashCode ] = LinkedList()
			# 옷의 종류 리스트에 추가
			type.append( data[1] )
		# 해당 해시코드의 연결리스트에 data값 삽입
		hashTable[ hashCode ].insertNode( data )

	# 가능한 모든 경우를 담을 리스트
	answer = []
	# 미완성 : fillAnswer( hashTable, size, type, answer )





clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution( clothes )