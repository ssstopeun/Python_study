from collections import deque

#direction 오른쪽 1, 아래 2, 왼쪽 3, 위 4
def snake_move(direction, location):
    snake_x, snake_y = location
    head_x, head_y = 0,0
    if direction == 1: #오른쪽으로 직진
        head_x,head_y = snake_x,snake_y + 1
    elif direction == 2: #아래로
        head_x, head_y = snake_x + 1, snake_y
    elif direction == 3: #왼쪽으로
        head_x, head_y = snake_x, snake_y - 1
    elif direction == 4: #위쪽으로
        head_x, head_y = snake_x - 1, snake_y

    # 벽에 부딪히지않고 뱀의 몸이 있지않은 자리일때
    if 0 <= head_x < groundSize and 0 <= head_y < groundSize and GameMap[head_x][head_y] != 1:
        #머리부분을 늘인다. 우선적으로 늘리고 사과가 없을때 꼬리를 줄여주기
        snake.append((head_x,head_y))

        if GameMap[head_x][head_y] != 5:
            tail_x,tail_y = snake.popleft()
            #꼬리 줄여주기
            GameMap[tail_x][tail_y] = 0
        #map에 뱀위치 1로 표시
        GameMap[snake_x][snake_y] = 1

    else: #벽이나 자기몸에 부딪혀서 게임종료
        return False
    return True

def direction_change(direction,change_direction):
    if change_direction == 1: #오른쪽으로 turn
        if direction == 1: #오른쪽으로 직진중일때 아래로 바뀜
            direction = 2
        elif direction == 2: #아래로 가고있을땐 왼쪽으로 바뀜
            direction = 3
        elif direction == 3: #왼쪽으로 가고있을땐 위로 바뀜
            direction = 4
        elif direction == 4: #위로가고있을땐 오른쪽으로 바뀜
            direction = 1

    elif change_direction == 3: #왼쪽으로 turn
        if direction == 1: #오른쪽으로 직진중일때 위로 바뀜
            direction = 4
        elif direction == 2: #아래로 가고있을땐 오른쪽으로 바뀜
            direction = 1
        elif direction == 3: #왼쪽으로 가고있을땐 아래로 바뀜
            direction = 2
        elif direction == 4: #위로가고있을땐 왼쪽으로 바뀜
            direction = 3

    return direction

if __name__ == '__main__':
    print("===============Input================")
    groundSize = int(input())
    appleCount = int(input())
    changeDirectionCount = int(input())

    # game의 맵 : 사과가 있으면 5
    GameMap = [[0 for _ in range(groundSize)] for _ in range(groundSize)]
    for i in range(appleCount):
        Location1, Location2 = map(int, input().split())
        #사과위치 5로 표시하기
        GameMap[Location1-1][Location2-1] = 5

    #방향전환
    changeTime = [0]*10000
    for i in range(changeDirectionCount):
        changeDirection1, changeDirection2 = input().split()
        if changeDirection2 == 'R':
            cd2 = 1 #오른쪽으로 회전
        else:
            cd2 = 3 #왼쪽으로 회전
        cd1 = int(changeDirection1)
        changeTime[cd1] = cd2


    # 뱀의 머리와 꼬리 : 앞쪽 인덱스 - 머리, 뒤쪽 인덱스 - 꼬리
    snake = deque([(0,0)])
    turn = 0 #지금이 무슨 turn인지
    direction = 1 #기본방향 (오른쪽으로 직진)

    while True:
        turn += 1
        #이동
        if snake_move(direction,snake[-1]) is False:
            break
        if changeTime[turn]:
            direction = direction_change(direction,changeTime[turn])

    print("===============Output================")
    print(turn)










