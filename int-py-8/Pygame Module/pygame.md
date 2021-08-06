# Python - Pygame

![](https://camo.githubusercontent.com/1971c0a4f776fb5351c765c37e59630c83cabd52/68747470733a2f2f7777772e707967616d652e6f72672f696d616765732f6c6f676f2e706e67)

## What is pygame ?

Pygame is a cross - platform set of python modules designed for writing video games.
It includes computer graphics and sound libraries designed to be used with the python programming language.

Pygame was officially written by **_Pete Shinners_** to replace PySDL .

Pygame is suitable to create client-side application that can be potenially wrapped in a standlone executable.

---

## Why pygame ?

- Built on top of the highly portable SDL (Simple DirectMedia Layer) development library, pygame can run across many platforms and operating systems.

- By using the pygame pygame module, you can control the logic and graphics of your games without worrying about the backend complexities required for working with video and audio.

---

## Pre-Requisites for Pygame

Pygame module comes with the latest vesion of Python 2 and Python 3. pip is the best method of installing it.

Use the command in command prompt

```python
pip install pygame
```

---

## Overview

Pygame is a free. Released under the LGPL licence, you can create open source, free ware, shareware and commercial games with it.

Some features about the pygame listed below

- Multi-core CPUs can be used easily.
- Uses optimized C and Assembly code for core functions.
- Comes with many operating systems.
- Truly portable.
- Its simple.
- Many games have been published.
- We can control the main loop.
- Does not require GUI to use all functions.
- Fast response to report bugs.
- Small amount of code.
- Modular.

---

## Some basic functions

- **import pygame**

   This provides access to the pygame framework and imports all functions of pygame.

- **pygame.init()**
  
   This is used to initialize all the required modules of the pygame.

- **pygame.display.set_mode((width, height))**

   This is used to display the window of the desired size. The return value is a Surface object which is the object where we will perform graphical operations.

- **pygame.QUIT**

   This is used to terminate the event when we click on the close button at the corner of the window.

- **tick()**

   This function is used to update the clock. The syntax is the following `tick(framerate = 0)`

- **get_time()**

   The get_time() is used to get the previous tick. The number of millisecond that is passed between the last two calls in Clock.tick()

- **blit()** 
  
   This function is used to draw one image into another. The draw can be placed with the dest argument.

- **pygame.Surface()**

   This function is to add an image on the window. 


---

## Pygame Vs Pyglet

Lets take a look on some difference why we are going for pygame instead of pyglet.

Some difference are listed below.


|Pygame|Pyglet|
|:--------:|:--------:|
|**_Easy Python Syntax_**  - Pygame uses python as a scripting language. Python is widely used treated as one of the most natural language to grasp. |**_3d Support_** -  since pyglet is so firmly merged with OpenGL. It allows support of drawing in 3D|
|**_Usage API_**   - The API is very straightforward|**_Cross-platform_**   - It can work Linux, Windows and OS X .|
|**_Best canvas system_**   - Pygame provides a draing system that allos the user to create and draw an unlimited number of canvas| **_Written in pure python_** - It can be compiled using any other python interpreters.|
|**_More Popular_** | **_Less Popular_**|
|||

---

## Program using pygame

![](https://www.pygame.org/ftp/pygame-head-party.png)



### CODING TIME !

```python
import pygame
import time
import random

pygame.init()

white    = (255, 255, 255)
yellow   = (255, 255, 102)
black    = (  0,   0,   0)
red      = (213,  50,  80)
green    = (  0, 255,   0)
blue     = ( 50, 153, 213)

dis_width  = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("banchscrifts", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Score : " +str(score), True, yellow)
    dis.blit(value, [0,0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0],x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6 , dis_height/3])

def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
gameLoop()
```

---

## Output

![Py-1Image](https://user-images.githubusercontent.com/70591317/126902101-6b53ebd0-c9c6-4c07-90f2-e5ed3da64048.png)


## Thank you

### Content By - Rammya Dharshini K

---
---
