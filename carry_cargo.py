import pgzrun

WIDTH = 700
HEIGHT = 490

map_data = [
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
]

player_location = [1, 0]
cargo_location = [1, 1]  # 荷物の現在位置
exit_location = [9, 6]
size = 70

status = 1  # 1開始 2:終了 3:判定
message = ''
time_count = 0  # 表示までのインターバル


player = Actor('player', topleft=(size, 0))
floor = Actor('floor', topleft=(0, 0))
box = Actor('box', topleft=(0, 0))
exit = Actor('exit', topleft=(630, 420))
cargo = Actor('cargo', topleft=(size*1, size*1))


def draw():
    screen.clear()
    if status == 3:
        screen.draw.text(message, (200, 220), color='orange', fontsize=72)
    else:
        for y in range(len(map_data)):
            for x in range(len(map_data[0])):
                floor.topleft = (size*x, size*y)
                floor.draw()
                if map_data[y][x] != 0:
                    box.topleft = (size*x, size*y)
                    box.draw()
        exit.draw()
        player.draw()
        cargo.draw()


def update():
    global status
    global time_count
    if status == 2:
        time_count += 1
        if time_count == 30:
            status = 3


def on_key_down(key):
    # プレイヤーの進行方向に荷物があるなら荷物が移動できるか調べ、移動出来たらプレイヤーも一緒に移動する
    # 荷物出ないならboxがあるか調べ、なければプレイヤーを移動する
    if key == key.UP:
        if player_location[1] > 0:
            if is_cargo(key):
                if is_push(key):
                    move(key, player_location, player)
            elif is_not_box(key, player_location):
                move(key, player_location, player)
    elif key == key.DOWN:
        if player_location[1] < len(map_data)-1:
            if is_cargo(key):
                if is_push(key):
                    move(key, player_location, player)
            elif is_not_box(key, player_location):
                move(key, player_location, player)
    elif key == key.LEFT:
        if player_location[0] > 0:
            if is_cargo(key):
                if is_push(key):
                    move(key, player_location, player)
            elif is_not_box(key, player_location):
                move(key, player_location, player)
    elif key == key.RIGHT:
        if player_location[0] < len(map_data[0])-1:
            if is_cargo(key):
                if is_push(key):
                    move(key, player_location, player)
            elif is_not_box(key, player_location):
                move(key, player_location, player)
    judgment()


"""
    if key == key.UP:
        if player_location[1] > 0 and is_not_box(key, player_location):
            move(key, player_location, player)

    elif key == key.DOWN:
        if player_location[1] < len(map_data) - 1 and is_not_box(key, player_location):
            move(key, player_location, player)

    elif key == key.LEFT:
        if player_location[0] > 0 and is_not_box(key, player_location):
            move(key, player_location, player)

    elif key == key.RIGHT:
        if player_location[0] < len(map_data[0]) - 1 and is_not_box(key, player_location):
            move(key, player_location, player)


"""

"""
    if key == key.UP:
        if player_location[1] > 0:  # プレイヤーが上端ではない
            if map_data[player_location[1]-1][player_location[0]] != 1:  # プレイヤーの進行方向にBoxが無い
                player_location[1] -= 1
                player.y -= size
    elif key == key.DOWN:
        if player_location[1] < len(map_data) - 1:  # プレイヤーが下端ではない
            if map_data[player_location[1]+1][player_location[0]] != 1:  # プレイヤーの進行方向にBoxが無い
                player_location[1] += 1
                player.y += size
    elif key == key.LEFT:
        if player_location[0] > 0:  # プレイヤーが左端ではない
            if map_data[player_location[1]][player_location[0]-1] != 1:  # プレイヤーの進行方向にBoxが無い
                player_location[0] -= 1
                player.x -= size
    elif key == key.RIGHT:
        if player_location[0] < len(map_data[0]) - 1:      # プレイヤーが右左端ではない
            if map_data[player_location[1]][player_location[0]+1] != 1:  # プレイヤーの進行方向にBoxが無い
                player_location[0] += 1
                player.x += size
"""


def is_not_box(key, location):
    if key == key.UP:
        if map_data[location[1]-1][location[0]] != 1:  # Actorの進行方向にBoxが無ければTrueを返す
            return True
    elif key == key.DOWN:
        if map_data[location[1]+1][location[0]] != 1:  # Actorの進行方向にBoxが無ければTrueを返す
            return True
    elif key == key.LEFT:
        if map_data[location[1]][location[0]-1] != 1:  # Actorの進行方向にBoxが無ければTrueを返す
            return True
    elif key == key.RIGHT:
        if map_data[location[1]][location[0]+1] != 1:  # Actorの進行方向にBoxが無ければTrueを返す
            return True
    return False


def is_cargo(key,):
    if key == key.UP:
        # プレイヤーの上に荷物があるときTrue
        if player_location[0] == cargo_location[0] and player_location[1]-1 == cargo_location[1]:
            return True
    elif key == key.DOWN:
        if player_location[0] == cargo_location[0] and player_location[1]+1 == cargo_location[1]:
            return True
    elif key == key.LEFT:
        if player_location[0]-1 == cargo_location[0] and player_location[1] == cargo_location[1]:
            return True
    elif key == key.RIGHT:
        if player_location[0]+1 == cargo_location[0] and player_location[1] == cargo_location[1]:
            return True
    return False


def is_push(key):
    if key == key.UP:
        # 荷物は上端ではなく、かつ荷物の上にboxがない
        if cargo_location[1] > 0 and is_not_box(key, cargo_location):
            move(key, cargo_location, cargo)
            return True

    elif key == key.DOWN:
        if cargo_location[1] < len(map_data) - 1 and is_not_box(key, cargo_location):
            move(key, cargo_location, cargo)
            return True

    elif key == key.LEFT:
        if cargo_location[0] > 0 and is_not_box(key, cargo_location):
            move(key, cargo_location, cargo)
            return True

    elif key == key.RIGHT:
        if cargo_location[0] < len(map_data[0]) - 1 and is_not_box(key, cargo_location):
            move(key, cargo_location, cargo)
            return True
    return False


def move(key, location, obj):
    if key == key.UP:  # キーの方向にActorを進める
        location[1] -= 1
        obj.y -= size
    elif key == key.DOWN:
        location[1] += 1
        obj.y += size
    elif key == key.LEFT:
        location[0] -= 1
        obj.x -= size
    elif key == key.RIGHT:
        location[0] += 1
        obj.x += size


def judgment():
    global status
    global message
    if cargo_location == exit_location and status == 1:  # ゲーム中かつ荷物と出口が重なった
        message = 'STAGE CLEAR'
        status = 2
    else:
        touch = 0  # 荷物の辺が壁や箱に触れている数
        x = cargo_location[0]  # 荷物のx,yの位置
        y = cargo_location[1]
        if x == 0 or x == len(map_data[0])-1:  # 荷物の左右が壁に接している
            touch += 1
        elif map_data[y][x-1] == 1 or map_data[y][x+1] == 1:  # 荷物の左右がboxに接している
            touch += 1
        if y == 0 or y == len(map_data)-1:  # 荷物の上下が壁に接している
            touch += 1
        elif map_data[y-1][x] == 1 or map_data[y+1][x] == 1:  # 荷物の上下がboxに接している
            touch += 1
        if touch > 1 and status == 1:
            message = 'GAME OVER'
            status = 2


pgzrun.go()
