import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

'''
Modeling pendulum.
'''

def theta(t, theta_0, theta_dot_0, mu, m, g, L):
    theta_ = theta_0
    theta_dot_ = theta_dot_0
    theta_dot_dot_ = 0
    delta_t = 0.01
    for time in np.arange(0, t, delta_t):
        theta_dot_dot_ = -mu * theta_dot_ - g * np.sin(theta_) / (m * L)
        theta_ += theta_dot_ * delta_t
        theta_dot_ += theta_dot_dot_ * delta_t
    return theta_, theta_dot_, theta_dot_dot_

def phase_space_vectors(tmin, tmax, dt):
    mu = 0.1
    g = 9.81
    m = 1
    L = 2

    vect = []
    for THETA_0 in np.arange(-2*np.pi, 2*np.pi, 0.5):
        for THETA_DOT_0 in np.arange(-10, 10, 1):
            tmp = []
            for t in np.arange(tmin, tmax, dt):
                theta_, theta_dot_, theta_dot_dot_ = theta(t, THETA_0, THETA_DOT_0, mu, m, g, L)
                tmp.append((theta_, theta_dot_, theta_dot_dot_))
            vect.extend(tmp[1:])

    return np.array(vect)

def plot_phase_space(vect, xlim, ylim, xlabel, ylabel):
    # color space
    color_number = 50
    colors = cm.get_cmap('plasma', color_number)

    # plot
    plt.xlim(-xlim, xlim)
    plt.ylim(-ylim, ylim)

    # t = theta
    # td = theta_dot
    # tdd = theta_dot_dot
    norm_scale = 0.2
    max_td = np.max(vect[:,1])
    max_tdd = np.max(vect[:,2])

    for t, td, tdd in vect:
        color_idx = int(np.interp(np.abs(td), [0, max_td], [0, color_number]))
        plt.arrow(
            t, td,
            td*norm_scale/max_td, tdd*norm_scale/max_tdd,
            head_width=0.03, head_length=0.1, length_includes_head=False,
            color=colors(color_idx)
        )

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# get data & plot
vect = phase_space_vectors(0, 1, 0.1)
plot_phase_space(vect, 10, 10, "theta", "theta dot")