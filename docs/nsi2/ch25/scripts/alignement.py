from PIL import Image
import pygame
from os import listdir
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
PADDING = 10


def aligner(x, y):
    n = len(x) + 1
    m = len(y) + 1
    score = [[(0, '', '') for _ in range(m)] for _ in range(n)]  # tableau des scores et des motifs obtenus

    for i in range(n):
        score[i][0] = (i, x[:i], '-' * i)

    for j in range(m):
        score[0][j] = (j, '-' * j, y[:j])

    for i in range(1, n):
        for j in range(1, m):
            if x[i - 1] == y[j - 1]:
                total, xmotif, ymotif = score[i - 1][j - 1]
                score[i][j] = (total, xmotif + x[i - 1], ymotif + y[j - 1])
            else:
                total1, xmotif1, ymotif1 = score[i][j - 1]
                total2, xmotif2, ymotif2 = score[i - 1][j]

                if total1 <= total2:
                    total = 1 + total1
                    xmotif = xmotif1 + '-'
                    ymotif = ymotif1 + y[j - 1]
                else:
                    total = 1 + total2
                    xmotif = xmotif2 + x[i - 1]
                    ymotif = ymotif2 + '-'

                score[i][j] = (total, xmotif, ymotif)

    return score[n - 1][m - 1]


X = "TTCACCAGAAAAGAACACGGTAGTTACGAGTCCAATATTGTTAAACCG"
Y = "TTCACGAAAAAGTAACGGGCCGATCTCCAATAAGTGCGACCGAG"
X = "INFORMATIQUE"
Y = "NUMERIQUE"
longueur, sol_X, sol_Y = aligner(X, Y)

pygame.init()
font = pygame.font.Font(pygame.font.match_font('consolas'), 32)
solution_graphiqueX = font.render(sol_X, True, BLACK, WHITE)
solution_graphiqueY = font.render(sol_Y, True, BLACK, WHITE)

w, h = solution_graphiqueX.get_size()
WIDTH = w + 2 * PADDING
HEIGHT = 2 * h + 3 * PADDING
window = pygame.display.set_mode((WIDTH, HEIGHT))
window.fill(WHITE)
pygame.display.flip()
clock = pygame.time.Clock()
go_on = True
debut_X = ""
debut_Y = ""
step = font.render("X", True, BLACK, WHITE).get_width()
print(step)
i = -2


def count_letters(s: str) -> int:
    return len([x for x in s if x != '-'])


def make_gif(folder):
    images = [Image.open(folder + '/' + file) for file in listdir(folder)]
    images[0].save('resul.gif', save_all=True, append_images=images[1:], optimize=True, duration=1000, loop=0)

while go_on:
    if i == -2:
        i += 1
    elif i < len(sol_X):
        debut_X = sol_X[i]
        debut_Y = sol_Y[i]
        fin_X = X[count_letters(sol_X[:i + 1]):]
        fin_Y = Y[count_letters(sol_Y[:i + 1]):]
        print(debut_X, '/', fin_X)
        print(debut_Y, '/', fin_Y)
        if debut_X == debut_Y:
            color = RED
        else:
            color = BLUE
        if i != -1:
            debut_X_G = font.render(debut_X, True, color, WHITE)
            debut_Y_G = font.render(debut_Y, True, color, WHITE)
            window.blit(debut_X_G, (PADDING + i * step, PADDING))
            window.blit(debut_Y_G, (PADDING + i * step, 2 * PADDING + h))

        fin_X_G = font.render(fin_X, True, BLACK, WHITE)
        fin_Y_G = font.render(fin_Y, True, BLACK, WHITE)

        window.blit(fin_X_G, (PADDING + (i + 1) * step, PADDING))
        window.blit(fin_Y_G, (PADDING + (i + 1) * step, 2 * PADDING + h))
        i += 1
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            go_on = False
    clock.tick(10)
    pygame.image.save(window,"tmp/"+str(i+1).zfill(3)+'.png')
pygame.quit()

make_gif('tmp')