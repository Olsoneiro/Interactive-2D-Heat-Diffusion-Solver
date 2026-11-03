# Interactive 2D Heat Diffusion Solver — Finite Difference Method (FDM)

A real-time, interactive Python simulation of two-dimensional heat conduction using the explicit **Finite Difference Method (FDM)**. Users can dynamically paint heat sources and heat sinks onto the 2D grid using their mouse and watch the thermal diffusion evolve live.

## Mathematical Formulation

The simulation solves the transient two-dimensional heat equation:

$$\frac{\partial u}{\partial t} = a \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where:
* $u(x, y, t)$ is the temperature field,
* $a$ is the thermal diffusivity coefficient.

### Numerical Scheme (Explicit FTCS)

The domain is discretized onto a uniform $N \times N$ grid ($N = 150$) with spatial steps $\Delta x = 1$, $\Delta y = 1$ and time step $\Delta t = 0.5$. Using Forward-Time Central-Space (FTCS) finite differences, the temperature at interior nodes is updated at each frame according to:

$$u_{i,j}^{(n+1)} = u_{i,j}^{(n)} + a \Delta t \left( \frac{u_{i+1,j}^{(n)} - 2u_{i,j}^{(n)} + u_{i-1,j}^{(n)}}{\Delta x^2} + \frac{u_{i,j+1}^{(n)} - 2u_{i,j}^{(n)} + u_{i,j-1}^{(n)}}{\Delta y^2} \right)$$

Dirichlet boundary conditions ($u = 0$) are maintained along the edges unless modified by the user's brush.

### Numerical Stability Criterion

To guarantee stability of the explicit scheme, the input thermal diffusivity $a$ must satisfy the two-dimensional Courant–Friedrichs–Lewy (CFL) / von Neumann stability condition:

$$a \left( \frac{\Delta t}{\Delta x^2} + \frac{\Delta t}{\Delta y^2} \right) \le 0.5$$

With the default parameters ($\Delta t = 0.5$, $\Delta x = \Delta y = 1$), the script enforces $a \le 0.5$ before launching the animation.

## Interactive Features

* **Left Mouse Button (LMB):** Click and drag to apply temperature $T_1$ (e.g., heat source) onto the canvas.
* **Right Mouse Button (RMB):** Click and drag to apply temperature $T_2$ (e.g., heat sink / cooling) onto the canvas.
* **Mouse Scroll Wheel:** Scroll up or down to dynamically resize the circular brush radius between $1$ and $20$ grid cells.

## Requirements

* Python 3.8+
* `numpy`
* `matplotlib`

Install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from your terminal:

```bash
python heat_diffusion.py
```

### Example Input Parameters

When prompted in the terminal, enter your simulation parameters:

```text
Enter thermal diffusivity coefficient: 0.4
Assign temperature value to LMB (Left Mouse Button): 100
Assign temperature value to RMB (Right Mouse Button): 0
```

Once the window opens, draw directly on the heatmap with your mouse to observe real-time heat transfer.