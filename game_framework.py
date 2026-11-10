import time
running = False
stack = []


def change_mode(mode):
    if stack:
        stack.pop().finish()
    stack.append(mode)
    mode.init()


def push_mode(mode):
    if stack:
        stack[-1].pause()
    stack.append(mode)
    mode.init()


def pop_mode():
    if stack:
        stack.pop().finish()
    if stack:
        stack[-1].resume()
    else:
        quit()


def quit():
    global running
    running = False

frame_time = 0.0

def run(start_mode):
    global running, stack, frame_time
    running = True
    stack = [start_mode]
    frame_time = 0.0

    try:
        start_mode.init()
        while running:
            frame_start = time.perf_counter()
            #time.sleep(0.7) #성능 최악 pc
            stack[-1].handle_events()
            stack[-1].update()
            stack[-1].render()
            frame_time = time.perf_counter() - frame_start
            frame_rate = 1.0 / frame_time if frame_time > 0 else 0.0
            #print(f'Frame Time: {frame_time}, Frame Rate: {frame_rate}')
            #time.sleep(0.02)
    finally:
        while stack:
            stack.pop().finish()
        running = False
