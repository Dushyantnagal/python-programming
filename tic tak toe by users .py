move =[' ',' ',' ',' ',' ',' ',' ',' ',' ']

print(f'''
 {move[0]}|{move[1]}|{move[2]}
 ------
 {move[3]}|{move[4]}|{move[5]}
 ------
 {move[6]}|{move[7]}|{move[8]}''')

turn='0'
while 1:
    player_in = int(input(f'{turn} turn Enter location 0-8: '))
    if move[player_in] != ' ':
        print('location already in use try again ')
        continue
    else:
        move [player_in] = turn

    if move[0] == move[1] == move[2] !=' ' :
        print(move[0], 'Win')
        break
    if move[3] == move[4] == move[5] !=' ' :
        print(move[0], 'Win')
        break
    if move[6] == move[7] == move[8] !=' ' :
        print(move[0], 'Win')
        break
    if move[0] == move[4] == move[8] !=' ' :
        print(move[0], 'Win')
        break
    if move[2] == move[4] == move[6] !=' ' :
        print(move[0], 'Win')
        break
    if move[0] == move[3] == move[6] !=' ' :
        print(move[0], 'Win')
        break
    if move[1] == move[4] == move[7] !=' ' :
        print(move[0], 'Win')
        break
    if move[2] == move[5] == move[8] !=' ' :
        print(move[0], 'Win')
        break
    if ' ' not in move :
        print('Match tie')
        break
    turn = 'x' if turn == '0' else '0'
    print(f'''
    {move[0]}|{move[1]}|{move[2]}
    ------
    {move[3]}|{move[4]}|{move[5]}
    ------
    {move[6]}|{move[7]}|{move[8]}''')

