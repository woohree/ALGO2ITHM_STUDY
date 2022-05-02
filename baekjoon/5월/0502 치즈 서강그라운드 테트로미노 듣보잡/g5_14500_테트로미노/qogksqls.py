import sys
sys.stdin = open('B.txt')

N, M = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]


# I_mino
def get_I_sero_mino_max():
    I_mino_moves = [3, 2, 1, 0]
    I_mino_max = 0
    for i in range(N):
        for j in range(M):
            I_mino = 0
            for I_mino_move in I_mino_moves:
                if i + I_mino_move < N:
                    I_mino += matrix[i + I_mino_move][j]
                else:
                    return I_mino_max
            I_mino_max = max(I_mino_max, I_mino)


def get_I_garo_mino_max():
    I_mino_moves = [3, 2, 1, 0]
    I_mino_max = 0
    for j in range(M):
        for i in range(N):
            I_mino = 0
            for I_mino_move in I_mino_moves:
                if j + I_mino_move < M:
                    I_mino += matrix[i][j + I_mino_move]
                else:
                    return I_mino_max
            I_mino_max = max(I_mino_max, I_mino)


# O_mino
def get_O_mino_max():
    O_mino_moves = [[0, 0], [1, 0], [0, 1], [1, 1]]
    O_mino_max = 0
    for j in range(M):
        for i in range(N):
            O_mino = 0
            for O_mino_move in O_mino_moves:
                if i + O_mino_move[0] < N and j + O_mino_move[1] < M:
                    O_mino += matrix[i + O_mino_move[0]][j + O_mino_move[1]]
            O_mino_max = max(O_mino_max, O_mino)
    return O_mino_max


# Z_mino
def get_Z_mino_max():
    Z_mino_moves1 = [[0, 0], [1, 0], [1, 1], [2, 1]]
    Z_mino_moves2 = [[0, 0], [1, 0], [1, -1], [2, -1]]
    Z_mino_moves3 = [[0, 0], [0, 1], [1, 1], [1, 2]]
    Z_mino_moves4 = [[0, 0], [0, 1], [-1, 1], [-1, 2]]
    Z_mino_max = 0
    for j in range(M):
        for i in range(N):
            Z_mino = 0
            for Z_mino_move in Z_mino_moves1:
                if 0 <= i + Z_mino_move[0] < N and 0 <= j + Z_mino_move[1] < M:
                    Z_mino += matrix[i + Z_mino_move[0]][j + Z_mino_move[1]]
            Z_mino_max = max(Z_mino_max, Z_mino)

    for j in range(M):
        for i in range(N):
            Z_mino = 0
            for Z_mino_move in Z_mino_moves2:
                if 0 <= i + Z_mino_move[0] < N and 0 <= j + Z_mino_move[1] < M:
                    Z_mino += matrix[i + Z_mino_move[0]][j + Z_mino_move[1]]
            Z_mino_max = max(Z_mino_max, Z_mino)

    for j in range(M):
        for i in range(N):
            Z_mino = 0
            for Z_mino_move in Z_mino_moves3:
                if 0 <= i + Z_mino_move[0] < N and 0 <= j + Z_mino_move[1] < M:
                    Z_mino += matrix[i + Z_mino_move[0]][j + Z_mino_move[1]]
            Z_mino_max = max(Z_mino_max, Z_mino)

    for j in range(M):
        for i in range(N):
            Z_mino = 0
            for Z_mino_move in Z_mino_moves4:
                if 0 <= i + Z_mino_move[0] < N and 0 <= j + Z_mino_move[1] < M:
                    Z_mino += matrix[i + Z_mino_move[0]][j + Z_mino_move[1]]
            Z_mino_max = max(Z_mino_max, Z_mino)

    return Z_mino_max


# L_mino
def get_L_mino_max():
    L_mino_moves1 = [[0, 0], [1, 0], [2, 0], [2, 1]]
    L_mino_moves2 = [[0, 0], [1, 0], [2, 0], [2, -1]]
    L_mino_moves3 = [[0, 0], [0, 1], [0, 2], [1, 2]]
    L_mino_moves4 = [[0, 0], [0, 1], [0, 2], [-1, 2]]
    L_mino_moves5 = [[0, 0], [0, 1], [1, 0], [2, 0]]
    L_mino_moves6 = [[0, 0], [0, 1], [1, 1], [2, 1]]
    L_mino_moves7 = [[0, 0], [1, 0], [1, 1], [1, 2]]
    L_mino_moves8 = [[0, 0], [-1, 0], [-1, 1], [-1, 2]]
    L_mino_max = 0
    for j in range(M):
        for i in range(N):
            L_mino = 0
            for L_mino_move in L_mino_moves1:
                if 0 <= i + L_mino_move[0] < N and 0 <= j + L_mino_move[1] < M:
                    L_mino += matrix[i + L_mino_move[0]][j + L_mino_move[1]]
            L_mino_max = max(L_mino_max, L_mino)

    for j in range(M):
        for i in range(N):
            L_mino = 0
            for L_mino_move in L_mino_moves2:
                if 0 <= i + L_mino_move[0] < N and 0 <= j + L_mino_move[1] < M:
                    L_mino += matrix[i + L_mino_move[0]][j + L_mino_move[1]]
            L_mino_max = max(L_mino_max, L_mino)

    for j in range(M):
        for i in range(N):
            L_mino = 0
            for L_mino_move in L_mino_moves3:
                if 0 <= i + L_mino_move[0] < N and 0 <= j + L_mino_move[1] < M:
                    L_mino += matrix[i + L_mino_move[0]][j + L_mino_move[1]]
            L_mino_max = max(L_mino_max, L_mino)

    for j in range(M):
        for i in range(N):
            L_mino = 0
            for L_mino_move in L_mino_moves4:
                if 0 <= i + L_mino_move[0] < N and 0 <= j + L_mino_move[1] < M:
                    L_mino += matrix[i + L_mino_move[0]][j + L_mino_move[1]]
            L_mino_max = max(L_mino_max, L_mino)
    for j in range(M):
        for i in range(N):
            L_mino = 0
            for L_mino_move in L_mino_moves5:
                if 0 <= i + L_mino_move[0] < N and 0 <= j + L_mino_move[1] < M:
                    L_mino += matrix[i + L_mino_move[0]][j + L_mino_move[1]]
            L_mino_max = max(L_mino_max, L_mino)
    for j in range(M):
        for i in range(N):
            L_mino = 0
            for L_mino_move in L_mino_moves6:
                if 0 <= i + L_mino_move[0] < N and 0 <= j + L_mino_move[1] < M:
                    L_mino += matrix[i + L_mino_move[0]][j + L_mino_move[1]]
            L_mino_max = max(L_mino_max, L_mino)
    for j in range(M):
        for i in range(N):
            L_mino = 0
            for L_mino_move in L_mino_moves7:
                if 0 <= i + L_mino_move[0] < N and 0 <= j + L_mino_move[1] < M:
                    L_mino += matrix[i + L_mino_move[0]][j + L_mino_move[1]]
            L_mino_max = max(L_mino_max, L_mino)
    for j in range(M):
        for i in range(N):
            L_mino = 0
            for L_mino_move in L_mino_moves8:
                if 0 <= i + L_mino_move[0] < N and 0 <= j + L_mino_move[1] < M:
                    L_mino += matrix[i + L_mino_move[0]][j + L_mino_move[1]]
            L_mino_max = max(L_mino_max, L_mino)
    return L_mino_max


# T_mino
def get_T_mino_max():
    T_mino_moves1 = [[0, 0], [1, 0], [2, 0], [1, 1]]
    T_mino_moves2 = [[0, 0], [1, 0], [2, 0], [1, -1]]
    T_mino_moves3 = [[0, 0], [0, 1], [0, 2], [1, 1]]
    T_mino_moves4 = [[0, 0], [0, 1], [0, 2], [-1, 1]]
    T_mino_max = 0
    for j in range(M):
        for i in range(N):
            T_mino = 0
            for T_mino_move in T_mino_moves1:
                if 0 <= i + T_mino_move[0] < N and 0 <= j + T_mino_move[1] < M:
                    T_mino += matrix[i + T_mino_move[0]][j + T_mino_move[1]]
            T_mino_max = max(T_mino_max, T_mino)
    for j in range(M):
        for i in range(N):
            T_mino = 0
            for T_mino_move in T_mino_moves2:
                if 0 <= i + T_mino_move[0] < N and 0 <= j + T_mino_move[1] < M:
                    T_mino += matrix[i + T_mino_move[0]][j + T_mino_move[1]]
            T_mino_max = max(T_mino_max, T_mino)
    for j in range(M):
        for i in range(N):
            T_mino = 0
            for T_mino_move in T_mino_moves3:
                if 0 <= i + T_mino_move[0] < N and 0 <= j + T_mino_move[1] < M:
                    T_mino += matrix[i + T_mino_move[0]][j + T_mino_move[1]]
            T_mino_max = max(T_mino_max, T_mino)
    for j in range(M):
        for i in range(N):
            T_mino = 0
            for T_mino_move in T_mino_moves4:
                if 0 <= i + T_mino_move[0] < N and 0 <= j + T_mino_move[1] < M:
                    T_mino += matrix[i + T_mino_move[0]][j + T_mino_move[1]]
            T_mino_max = max(T_mino_max, T_mino)
    return T_mino_max


result = []
result.append(get_I_sero_mino_max())
result.append(get_I_garo_mino_max())
result.append(get_O_mino_max())
result.append(get_Z_mino_max())
result.append(get_L_mino_max())
result.append(get_T_mino_max())

print(max(result))
