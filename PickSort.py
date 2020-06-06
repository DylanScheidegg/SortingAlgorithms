from Settings import *
from Button import Button
import random


class StartMenu(object):
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.bgX = 0
        self.window = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.transform.scale(bg, (self.width, self.height))
        self.bgX2 = self.bg.get_width()

        self.bubble_sort = Button((255, 255, 255), self.width // 3 - 300, self.height // 2 - 150, 250, 50, 60,
                                  'Bubble Sort')
        self.gnome_sort = Button((255, 255, 255), self.width // 3, self.height // 2 - 150, 250, 50, 60, 'Gnome Sort')
        self.insertion_sort = Button((255, 255, 255), self.width // 3 + 300, self.height // 2 - 150, 280, 50, 60,
                                     'Insertion Sort')
        self.pigeonhole_sort = Button((255, 255, 255), self.width // 3 - 200, self.height // 2 - 50, 320, 50, 60,
                                      'Pigeonhole Sort')
        self.selection_sort = Button((255, 255, 255), self.width // 3 + 200, self.height // 2 - 50, 300, 50, 60,
                                     'Selection Sort')
        self.quit_game_button = Button((255, 255, 255), self.width // 3 - 300, self.height // 2 + 100, 150, 50, 40,
                                       'Quit Game')

    def loading_screen(self):
        close_loading = True
        r_col = 0
        g_col = 0
        b_col = 0
        while close_loading:
            if r_col == 255 and g_col < 255:
                rand_color = (r_col, g_col, b_col)
                if g_col >= 255:
                    g_col = 255
                else:
                    g_col += 5
            elif r_col == 255 and g_col == 255 and b_col < 255:
                rand_color = (r_col, g_col, b_col)
                if b_col >= 255:
                    b_col = 255
                else:
                    b_col += 5
            elif r_col == 255 and g_col == 255 and b_col == 255:
                rand_color = (r_col, g_col, b_col)
                r_col, g_col, b_col = 0, 0, 0
            else:
                rand_color = (r_col, g_col, b_col)
                if r_col >= 255:
                    r_col = 255
                else:
                    r_col += 5

            self.bgX -= 1.4
            self.bgX2 -= 1.4

            if self.bgX < self.bg.get_width() * -1:
                self.bgX = self.bg.get_width()

            if self.bgX2 < self.bg.get_width() * -1:
                self.bgX2 = self.bg.get_width()

            self.window.blit(self.bg, (self.bgX, 0))
            self.window.blit(self.bg, (self.bgX2, 0))

            large_font = pygame.font.SysFont('twcencondensed', 80)
            small_font = pygame.font.SysFont('twcencondensed', 40)
            render1 = large_font.render('Pick an Algorithm', 1, rand_color)
            render2 = small_font.render('Press Escape in any sorting method to go back to main screen', 1, rand_color)
            self.window.blit(render1, (self.width // 3, 100))
            self.window.blit(render2, (self.width // 5, self.height - 100))

            self.bubble_sort.draw(self.window, (0, 0, 0))
            self.gnome_sort.draw(self.window, (0, 0, 0))
            self.insertion_sort.draw(self.window, (0, 0, 0))
            self.pigeonhole_sort.draw(self.window, (0, 0, 0))
            self.selection_sort.draw(self.window, (0, 0, 0))
            self.quit_game_button.draw(self.window, (0, 0, 0))

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.bubble_sort.isOver(pos):
                        self.bubble()
                        close_loading = False
                    elif self.gnome_sort.isOver(pos):
                        self.gnome()
                        close_loading = False
                    elif self.insertion_sort.isOver(pos):
                        self.insertion()
                        close_loading = False
                    elif self.pigeonhole_sort.isOver(pos):
                        self.pigeonhole()
                        close_loading = False
                    elif self.selection_sort.isOver(pos):
                        self.selection()
                        close_loading = False
                    elif self.quit_game_button.isOver(pos):
                        pygame.quit()
                        quit()

                elif event.type == pygame.MOUSEMOTION:
                    if self.bubble_sort.isOver(pos):
                        self.bubble_sort.color = rand_color
                    elif self.gnome_sort.isOver(pos):
                        self.gnome_sort.color = rand_color
                    elif self.insertion_sort.isOver(pos):
                        self.insertion_sort.color = rand_color
                    elif self.pigeonhole_sort.isOver(pos):
                        self.pigeonhole_sort.color = rand_color
                    elif self.selection_sort.isOver(pos):
                        self.selection_sort.color = rand_color
                    elif self.quit_game_button.isOver(pos):
                        self.quit_game_button.color = rand_color

            pygame.display.update()

    def show(self, height):
        x = 25
        for i in range(len(height)):
            time.sleep(0.01)
            pygame.draw.rect(self.window, (0, 0, 0), (x, 25, 10, height[i]))
            pygame.display.update()
            x += 50

    def bubble(self):
        self.window.fill([255, 255, 255])
        pygame.display.update()

        arr = []
        for x in range(self.width // 50):
            rand_size = random.randint(50, 500)
            arr.append(rand_size)
        print(arr)

        bubble = True
        self.show(arr)
        time.sleep(5)
        count = 0
        n = len(arr)
        while bubble:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif pressed[pygame.K_ESCAPE]:
                    self.loading_screen()
                    bubble = False

            for i in range(n - 1):
                for j in range(0, n - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        print(arr)
                        self.show(arr)
                        self.window.fill([255, 255, 255])
                        small_font = pygame.font.SysFont('twcencondensed', 40)
                        render1 = small_font.render(str(count) + "Iterations", 1, (0, 0, 0))
                        self.window.blit(render1, (self.width // 5, self.height - 100))
                    count += 1

    def gnome(self):
        self.window.fill([255, 255, 255])
        pygame.display.update()

        arr = []
        for x in range(self.width // 50):
            rand_size = random.randint(50, 500)
            arr.append(rand_size)
        print(arr)

        gnome = True
        self.show(arr)
        time.sleep(5)
        n = len(arr)
        index = 0
        count = 0
        while gnome:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif pressed[pygame.K_ESCAPE]:
                    self.loading_screen()
                    gnome = False

            while index < n:
                if index == 0:
                    index = index + 1
                if arr[index] >= arr[index - 1]:
                    index = index + 1
                else:
                    arr[index], arr[index - 1] = arr[index - 1], arr[index]
                    index = index - 1
                count += 1
                small_font = pygame.font.SysFont('twcencondensed', 40)
                render1 = small_font.render(str(count) + "Iterations", 1, (0, 0, 0))
                self.window.fill([255, 255, 255])
                self.window.blit(render1, (self.width // 5, self.height - 100))
                self.show(arr)
                print(arr)
                pygame.display.update()

    def insertion(self):
        self.window.fill([255, 255, 255])
        pygame.display.update()

        arr = []
        for x in range(self.width // 50):
            rand_size = random.randint(50, 500)
            arr.append(rand_size)
        print(arr)

        merge = True
        self.show(arr)
        time.sleep(5)
        count = 0
        while merge:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif pressed[pygame.K_ESCAPE]:
                    self.loading_screen()
                    merge = False

            for i in range(1, len(arr)):
                key = arr[i]
                j = i - 1
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                    count += 1
                    small_font = pygame.font.SysFont('twcencondensed', 40)
                    render1 = small_font.render(str(count) + "Iterations", 1, (0, 0, 0))
                    self.window.fill([255, 255, 255])
                    self.window.blit(render1, (self.width // 5, self.height - 100))
                    self.show(arr)
                    print(arr)
                    pygame.display.update()
                arr[j + 1] = key

    def pigeonhole(self):
        self.window.fill([255, 255, 255])
        pygame.display.update()

        arr = []
        for x in range(self.width // 50):
            rand_size = random.randint(50, 500)
            arr.append(rand_size)
        print(arr)

        pigeonhole = True
        self.show(arr)
        time.sleep(5)
        count1 = 0

        my_min = min(arr)
        my_max = max(arr)
        size = my_max - my_min + 1
        holes = [0] * size
        for x in arr:
            assert type(x) is int, "integers only please"
            holes[x - my_min] += 1
        i = 0

        while pigeonhole:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif pressed[pygame.K_ESCAPE]:
                    self.loading_screen()
                    pigeonhole = False

            for count in range(size):
                while holes[count] > 0:
                    holes[count] -= 1
                    arr[i] = count + my_min
                    self.show(arr)
                    i += 1
                    count1 += 1
                    small_font = pygame.font.SysFont('twcencondensed', 40)
                    render1 = small_font.render(str(count1) + "Iterations", 1, (0, 0, 0))
                    self.window.fill([255, 255, 255])
                    self.window.blit(render1, (self.width // 5, self.height - 100))
                    self.show(arr)
                    print(arr)
                    pygame.display.update()

    def selection(self):
        self.window.fill([255, 255, 255])
        pygame.display.update()

        arr = []
        for x in range(self.width // 50):
            rand_size = random.randint(50, 500)
            arr.append(rand_size)
        print(arr)

        selection = True
        self.show(arr)
        time.sleep(5)
        count = 0
        while selection:
            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif pressed[pygame.K_ESCAPE]:
                    self.loading_screen()
                    selection = False

            for i in range(len(arr)):
                min_idx = i
                for j in range(i + 1, len(arr)):
                    if arr[min_idx] > arr[j]:
                        min_idx = j
                        count += 1
                        small_font = pygame.font.SysFont('twcencondensed', 40)
                        render1 = small_font.render(str(count) + "Iterations", 1, (0, 0, 0))
                        self.window.fill([255, 255, 255])
                        self.window.blit(render1, (self.width // 5, self.height - 100))
                        self.show(arr)
                        print(arr)
                        pygame.display.update()
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
