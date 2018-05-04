"""

Path tracking simulation with pure pursuit steering control and proportional speed control

author: Atsushi Sakai (@Atsushi_twi)

"""
import numpy as np
import math
import matplotlib.pyplot as plt
from src import setup


cal = setup.cal_load()

k = cal.cal_get('pp_k') #0.1  # look forward gain [s], used with state.v to add to look ahead Lfc
Lfc = 2.6  # look-ahead distance [m] distance ahead of the nearest course point
Kp = 1.0  # speed propotional gain
dt = 0.1  # [s]
L = 2.9  # [m] wheel base of vehicle

show_animation = True


class State:

    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        ''' state of position, yaw, and velocity object
        Parameters
        ----------
        state.x : x position component
        state.y : y position component
        state.yaw : yaw component
        state.v : velocity component
        
        Return
        ------
        state object with x, y, yaw, v components
        '''
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v


def update(state, a, delta):
    ''' unneeded in real test as vehicle will update state from GPS + encoders
        updates state based on speed adjustment from PIDcontrol and 
        pure_pursuit_control() delta
    '''
#    position updates
    state.x = state.x + state.v * math.cos(state.yaw) * dt
    state.y = state.y + state.v * math.sin(state.yaw) * dt
#    heading update
    state.yaw = state.yaw + state.v / L * math.tan(delta) * dt
#    velocity update
    state.v = state.v + a * dt

    return state


def PIDControl(target, current):
    ''' proportional speed control based on current and target speed
    Parameters
    ----------
    target : target speed [unitless, input = output, units must match current]
    current : current speed [unitless, input = output, units must match target]

    Returns
    -------
    a : adjustment in speed [unitless, input = output]
    '''
    a = Kp * (target - current)

    return a


def pure_pursuit_control(state, cx, cy, pind):
    '''
    1. calculate ind, which is target index
    2. if pind arguement is further along course, use pind as target index
    3. ensure index is not beyond end of course, otherwise set to course end
        get target x and y from course
    4. compute yaw (angle [radians]) needed to transition from state.x,y,yaw 
        to target x,y accounting for current yaw, atan2 takes into account sign
        of inputs, yaw from atan2 is in reference to x axis
    5. if state.v is reverse (negative) yaw should flip by pi rads
    6. distance to look ahead, based on constant Lfc[m] look forward constant
        + additional distance based on current velocity and k[s] look forward 
        gain
    7. compute desired yaw taking into account wheelbase and look ahead dist
        I'M DON'T TOTALLY UNDERSTAND THIS, TO BE RETURNED TO
    
    
    Parameters
    ----------
    state : state object
    cx : course x
    cy : course y
    pind : index of target course point
    
    Return
    ------
    delta : yaw in radians to set as heading to reach target coordinates
    ind : index of course target coordinates
    '''
#    1.
    ind = calc_target_index(state, cx, cy)

#    2. this might be unneeded or unwanted, 
    if pind >= ind:
        ind = pind
#    3.
    if ind < len(cx):
        tx = cx[ind]
        ty = cy[ind]
    else:
        tx = cx[-1]
        ty = cy[-1]
        ind = len(cx) - 1
#    4.
    alpha = math.atan2(ty - state.y, tx - state.x) - state.yaw
#    5.
    if state.v < 0:  # back
        alpha = math.pi - alpha
#    6.
    Lf = k * state.v + Lfc
#    7.
    delta = math.atan2(2.0 * L * math.sin(alpha) / Lf, 1.0)

    return delta, ind


def calc_target_index(state, cx, cy):
    ''' calcuate index of course which will be the updated target point
    
    1. find nearest point to current position which lies upon course path
    2. compute distance from point found in 1. to be used as target based on
        constant parameter and state.v[elocity] * gain
    3.compute distance between next point on course, if distance > distance 
        found in 2. return this index as the target index, if not, add next idx
    
    Parameters
    ----------
    state : state object x,y positions, velocity, yaw
    cx : course x
    cy : course y
    
    Return
    ------
    index of cx and cy which is the target index
    '''
    # compute list of current state x, y, vs target cx, cy for each point
    dx = [state.x - icx for icx in cx]
    dy = [state.y - icy for icy in cy]
#    compute hypotenuse length of dx dy right triange for each dx dy pair
    d = [abs(math.sqrt(idx ** 2 + idy ** 2)) for (idx, idy) in zip(dx, dy)]
#    find closest point along target course
    ind = d.index(min(d))
    L = 0.0
    print('L starting at : ' + str(L))

#    distance to look ahead, based on constant Lfc[m] look forward constant
#    + additional distance based on current velocity and k[s] look forward gain
    Lf = k * state.v + Lfc
    print('Lf starting at : ' + str(Lf))
    
    # search look ahead target point index
    while Lf > L and (ind + 1) < len(cx):
        dx = cx[ind + 1] - cx[ind]
        dy = cx[ind + 1] - cx[ind]
#        print('dx and dy : ' + str(dx) + ' - ' + str(dy))
        L += math.sqrt(dx ** 2 + dy ** 2)
#        print('L = ' + str(L))
        ind += 1
        print('index : ' + str(ind))

    return ind


def main():
    #  generate a sample target course
    cx = np.arange(0, 50, 0.1)
    cy = [math.sin(ix / 5.0) * ix / 2.0 for ix in cx]

    target_speed = 10.0 / 3.6  # [m/s]

    T = 100.0  # max simulation time

    # initial state
    state = State(x=0.5, y=-3.0, yaw=0.0, v=0.0)

    lastIndex = len(cx) - 1
    time = 0.0
    x = [state.x]
    y = [state.y]
    yaw = [state.yaw]
    v = [state.v]
    t = [0.0]
    target_ind = calc_target_index(state, cx, cy)

    while T >= time and lastIndex > target_ind:
#        ai = adustment in speed
        ai = PIDControl(target_speed, state.v)
#        di = 
        di, target_ind = pure_pursuit_control(state, cx, cy, target_ind)
        state = update(state, ai, di)

        time = time + dt

        x.append(state.x)
        y.append(state.y)
        yaw.append(state.yaw)
        v.append(state.v)
        t.append(time)

        if show_animation:
            plt.cla()
            plt.plot(cx, cy, ".r", label="course")
            plt.plot(x, y, "-b", label="trajectory")
            plt.plot(cx[target_ind], cy[target_ind], "xg", label="target")
            plt.axis("equal")
            plt.grid(True)
            plt.title("Speed[km/h]:" + str(state.v * 3.6)[:4])
            plt.pause(0.001)        
            plt.show()

    # Test
    assert lastIndex >= target_ind, "Cannot goal"

    if show_animation:
        plt.plot(cx, cy, ".r", label="course")
        plt.plot(x, y, "-b", label="trajectory")
        plt.legend()
        plt.xlabel("x[m]")
        plt.ylabel("y[m]")
        plt.axis("equal")
        plt.grid(True)

        flg, ax = plt.subplots(1)
        plt.plot(t, [iv * 3.6 for iv in v], "-r")
        plt.xlabel("Time[s]")
        plt.ylabel("Speed[km/h]")
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    print("Pure pursuit path tracking simulation start")
    main()
