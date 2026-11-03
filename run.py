import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

N = 150
size = 5
dt = 0.5
dx = 1
dy = 1

while True:
    a = float(input("Enter thermal diffusivity coefficient: "))
    b = (dt / dx**2) + (dt / dy**2)
    if a * b <= 0.5:
        break
    elif a * b > 0.5:
        print("The provided coefficient is too large!")

T1 = float(input("Assign temperature value to LMB (Left Mouse Button): "))
T2 = float(input("Assign temperature value to RMB (Right Mouse Button): "))

u = np.zeros((N, N))

fig, ax = plt.subplots(figsize=(8, 7))
im = ax.imshow(u, cmap='jet', vmin=T2, vmax=T1, origin='lower', animated=True)
cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label("Temperature", rotation=270, labelpad=15)

def update_title():
    ax.set_title(
        f"LMB: {T1} deg C | RMB: {T2} deg C | Brush size: {size}\n"
        f"(Use mouse scroll to change brush size)"
    )

update_title()
ax.axis('off')

is_drawing = False
current_pen_value = 0.0

def on_press(event):
    global is_drawing, current_pen_value
    if event.inaxes == ax:
        if event.button == 1:
            current_pen_value = T1
            is_drawing = True
            apply_temperature(event.xdata, event.ydata)
        elif event.button == 3:
            current_pen_value = T2
            is_drawing = True
            apply_temperature(event.xdata, event.ydata)

def on_release(event):
    global is_drawing
    is_drawing = False

def on_motion(event):
    if is_drawing and event.inaxes == ax:
        apply_temperature(event.xdata, event.ydata)

def on_scroll(event):
    global size
    if event.inaxes == ax:
        if event.button == 'up':
            size = min(size + 1, 20)
        elif event.button == 'down':
            size = max(size - 1, 1)

        update_title()
        fig.canvas.draw_idle()

def apply_temperature(x, y):
    global u
    if x is None or y is None:
        return

    ix, iy = int(x + 0.5), int(y + 0.5)

    for i in range(-size, size + 1):
        for j in range(-size, size + 1):
            if 0 <= ix + i < N and 0 <= iy + j < N:
                if i**2 + j**2 <= size**2:
                    u[iy + j, ix + i] = current_pen_value

def fdm(frame):
    global u
    u_next = u.copy()

    u_next[1:-1, 1:-1] = u[1:-1, 1:-1] + a * dt * (
        (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[:-2, 1:-1]) / dy**2 +
        (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, :-2]) / dx**2
    )

    u = u_next
    im.set_array(u)
    return [im]

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('scroll_event', on_scroll)

ani = animation.FuncAnimation(fig, fdm, interval=10, blit=True)

plt.show()