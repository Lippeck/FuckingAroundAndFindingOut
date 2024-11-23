class Drone:
    _velocity = 0
    _height_acc = 0
    _x_acc = 0
    _x = 0
    _height = 0
    _gravity = 10
    
    
    def __init__(self, velocity, acceleration, height, gravity, x_acc=0, x=0):
        self._velocity = velocity
        self._height_acc = acceleration
        self._height = height
        self._gravity = gravity
        self._x_acc = x_acc
        self._x = x
        
    def set_x_acc(self, x_acc):
        self._x_acc = x_acc
        
    def get_x_acc(self):
        return self._x_acc
    
    def set_x(self, x):
        self._x = x
    
    def set_height_acc(self, acc):
        self._height_acc = acc
        
    def get_acc(self):
        return self._height_acc
        
    def get_gravity(self):
        return self._gravity
        
    def get_velocity(self):
        return self._velocity
    
    def get_height(self):
        return self._height
    
    def fly(self):
        change = self._height_acc - self._gravity
        self._velocity += change
        self._height += self._velocity
        
    def get_velocity_after_acceration(self, acc):
        return self._velocity + acc - self._gravity
    
    def copy(self):
        return Drone(self._velocity, self._height_acc, self._height, self._gravity)
        
class DroneController:
    min_acc = 0
    max_acc = 20
    target_height = 0
    ticks = 0
    max_ticks = 0
    x_target = 0
    
    accelerations_applied = []
    
    def get_accelerations_applied(self):
        return self.accelerations_applied
    
    def __init__(self, drone, target_height, min_acc, max_acc, max_ticks, x_target):
        self.drone = drone
        self.target_height = target_height
        self.min_acc = min_acc
        self.max_acc = max_acc
        self.max_ticks = max_ticks
        self.x_target = x_target
        self.accelerations_applied = []    
        
    def do_the_thing(self, task):
        for acc in task:
            self.drone.set_height_acc(acc)
            self.drone.fly()
        return self.drone.get_height()
    
    def _apply_acceleration(self, required_acc, x_acc=0):
        self.accelerations_applied.append(required_acc)
        self.drone.set_x_acc(x_acc)
        self.drone.set_height_acc(required_acc)
        self.drone.fly()
        self.ticks += 1
        #print(f"{self.ticks}:{self.drone.get_height()}m, vel: {self.drone.get_velocity()}, apllied acc: {required_acc}")
    
    def reach_height(self):
        while self.drone.get_height() < self.target_height:
            if self._we_reach_height(self.target_height):
                next_acc = self.min_acc
            else:
                next_acc = self.max_acc
            self._apply_acceleration(next_acc)    
        #print(f"Max Height reached: {self.drone.get_height()}, max_height: {self.target_height}" ) 
        return self.drone.get_height()
    
    def wait_until_drone_drops(self):
        while self.drone.get_velocity() > 0 and self.ticks < self.max_ticks:
            self._apply_acceleration(self.min_acc)
        #print("Drone dropping!")
        return self.drone.get_height()
    
    def land_safely(self):
        while self.drone.get_height() > 0 and self.ticks < self.max_ticks:
            if self._do_we_crash_if_we_wait_and_full_throttle():
                if(self.drone.get_velocity_after_acceration(self.max_acc) < 0):
                    next_acc = self.max_acc
                else:
                    next_acc = - self.drone.get_velocity() + self.drone.get_gravity()
                    self._apply_acceleration(next_acc)
                    return self.engage_landing_sequence()
            else:
                next_acc = self.min_acc
            self._apply_acceleration(next_acc)
        return self.drone.get_height()
    
    def engage_landing_sequence(self):
        while self.drone.get_height() > 0 and self.ticks < self.max_ticks:
            next_acc = self.drone.get_gravity()
            self._apply_acceleration(next_acc)
        #print(f"Drone landed at height: {self.drone.get_height()}")
        return self.drone.get_height()
    
    def steer_towards_target_platform(self, x_target):
        while self.drone.get_x() != x_target and self.ticks < self.max_ticks:
            self.drone.set_height_acc(self.drone.get_gravity())
            self.drone.set_x_acc(x_target - self.drone.get_x())
            self.drone.fly()
            self.ticks += 1
        return self.drone.get_x()
    
    def _do_we_crash_if_we_wait_and_full_throttle(self):
        fly_calls = 0
        drone_copy = self.drone.copy()
        drone_copy.set_height_acc(0)
        drone_copy.fly()
        drone_copy.fly()
        fly_calls += 2
        prev_height = drone_copy.get_height()
        while drone_copy.get_height() >= 0 and prev_height >= drone_copy.get_height():
            prev_height = drone_copy.get_height()
            drone_copy.set_height_acc(self.max_acc)
            drone_copy.fly()
            fly_calls += 1
        return drone_copy.get_height() <= 0
    
    def _we_reach_height(self, target_height):
        drone_copy = self.drone.copy()
        prev_height = drone_copy.get_height()
        while drone_copy.get_height() < target_height and prev_height <= drone_copy.get_height() and drone_copy.get_height() >= 0:
            prev_height = drone_copy.get_height()
            drone_copy.set_height_acc(0)
            drone_copy.fly()
        return drone_copy.get_height() >= target_height
            
    def _do_we_overshoot_x_if_we_keep_accerlating(self):
        drone_copy = self.drone.copy()
        prev_x = drone_copy.get_x()
        while drone_copy.get_x() != self.x_target and prev_x <= drone_copy.get_x():
            prev_x = drone_copy.get_x()
            drone_copy.set_height_acc(self.drone.get_gravity())
            drone_copy.set_x_acc(self.max_acc - self.drone.get_gravity())
            drone_copy.fly()
        return drone_copy.get_x() != self.x_target