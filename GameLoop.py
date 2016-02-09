import time
import math

#This is our wiggle room. The lower we set it the more accurate our simulation is
#but the longer it takes simulation time to "catch up" to the real world. It can't
#be lower than how long it takes to complete the update or we'll never finish. The
#longer it is the more extrapolation our renderer is forced to do and the crappier
#it appears.
MS_PER_UPDATE = 15

#we'll simulate the real-world time the CPU takes to handle our program
#during its update and render phases with sleep() and these vars
render_cost_s=0.005
update_cost_s=0.010

lag_ms = 0.0 #how far behind our program is from what's rendered

#Our simulation's "state"
the_value = 0.0
goal_value = 255
completetion_time = 5000
increment = goal_value / (completetion_time / MS_PER_UPDATE)

#keep track of some stats
updates = 0
renders = 0

def get_current_time():
    import datetime as dt
    time_tpl = dt.datetime.now()
    return time_tpl

def get_time_in_ms(dttm):
    #We'll assume there's no way more than a minute has passed
    time_ms = (dttm.seconds*1e3) + (dttm.microseconds/1e3)
    return time_ms

def update():
    global updates, the_value
    the_value += increment
    updates += 1
    time_consuming_action(update_cost_s)
    return
def render(fraction):
    print(str(the_value+increment*fraction))
    global renders
    renders += 1
    time_consuming_action(render_cost_s)
    return
def time_consuming_action(value):
    #time.sleep(value)#comment here to see our program's "benchmark"
    return

#Thar she is. S'beautiful!
previous = get_current_time()
first = previous
while (the_value<goal_value):
    current = get_current_time()
    elapsed_ms = get_time_in_ms(current - previous)
    previous = current
    lag_ms += elapsed_ms
    while (lag_ms >= MS_PER_UPDATE):
        update()
        lag_ms -= MS_PER_UPDATE
    render(lag_ms / MS_PER_UPDATE)

total_time_elapsed = (get_current_time() - first)
print("Completed (" + str(updates) + ") updates and (" + str(renders) + ") renders in (" + str(total_time_elapsed) + ") for an AVG framerate of " + str(math.ceil(renders/(total_time_elapsed.seconds+total_time_elapsed.microseconds/1e6))))
