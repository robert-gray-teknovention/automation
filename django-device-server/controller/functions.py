import time


def pump_run(pump, duration, callback):
    print("We are running")
    print("Duration ", duration)
    # gpio.output(pump, PUMP_ON)
    time.sleep(duration)
    print("We are finished")
    callback()
    # gpio.output(pump, PUMP_OFF)


def light_control(socket, state, callback):
    print("We are turning the lights ", state)
    callback()
    # gpio.output(socket, state)


def output_run_duration(pin, on_state, duration, callback):
    print(pin, ' ', on_state, ' ', duration)
    # gpio.output(pin, on_state)
    time.sleep(duration)
    callback()
    '''if on_state == gpio.LOW:
        gpio.output(pin, gpio.HIGH)
   else:
       gpio.output(pin, gpio.LOW)'''


def output_control(pin, on_off, callback):
    print("Pin", pin, "ON" if on_off else "OFF")
    callback()
    # gpio.output(pin, on_off)
