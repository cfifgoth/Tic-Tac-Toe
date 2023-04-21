def coordinates_a_move():
    global field_state
    try:
        user_input_coordinates = input()
        x, y = user_input_coordinates.split()
        x = int(x)
        y = int(y)
        if not (x in [1,2,3] and y in [1,2,3]):
            print('Coordinates should be from 1 to 3!')
            x, y = coordinates_a_move()
        elif field_state_list[x - 1][y - 1] != '_':
            # print('> ', x, y)
            print('This cell is occupied! Choose another one!')
            x, y = coordinates_a_move()
    except ValueError:
        # print('> ', user_input_coordinates)
        print('You should enter numbers!')
        x, y = coordinates_a_move()
    finally:
        # print(user_input_coordinates)
        return x, y


def print_field_state():
    global field_state_list
    s_ = '---------'
    s_1 = '|' + field_state_list[0] + '|'
    s_2 = '|' + field_state_list[1] + '|'
    s_3 = '|' + field_state_list[2] + '|'
    print(s_)
    print(*s_1, ' ')
    print(*s_2, ' ')
    print(*s_3, ' ')
    print(s_)


def make_a_move():
    global field_state
    global field_state_list
    global current_user_id
    if field_state == '_________':
        print_field_state()
    current_user_id = 'X' if current_user_id in ['', 'O'] else 'O'
    x, y = coordinates_a_move()
    li = list(field_state_list[x - 1])
    li[y - 1] = current_user_id
    field_state_list[x - 1] = ''.join(li)
    # field_state_list[x - 1][y - 1] = current_user_id
    field_state = ''.join(field_state_list)
    print_field_state()
    end_game = game_state()
    if end_game:
        return
    else:
        make_a_move()



def game_state():
    global field_state
    win_cases_ = [field_state[0:3], field_state[3:6], field_state[6:9], field_state[0] + field_state[3] + field_state[6], field_state[1] + field_state[4] + field_state[7],
                  field_state[2] + field_state[5] + field_state[8], field_state[0] + field_state[4] + field_state[8], field_state[6] + field_state[4] + field_state[2]]
    if ("XXX" in win_cases_ and "OOO" in win_cases_) or abs(field_state.count("X") - field_state.count("O")) >= 2:
        print("Impossible")
        return True
    elif "_" not in field_state and "XXX" not in win_cases_ and "OOO" not in win_cases_:
        print("Draw")
        return True
    elif "_" in field_state and "XXX" not in win_cases_ and "OOO" not in win_cases_:
        # print("Game not finished")
        return False
    elif "XXX" in win_cases_:
        print("X wins")
        return True
    elif "OOO" in win_cases_:
        print("O wins")
        return True


field_state = '_________'
field_state_list = ['___', '___', '___']
current_user_id = ''
make_a_move()


if __name__ == '__main__':
    make_a_move()

