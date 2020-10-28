class EulerEstimator:
    def __init__(self, derivative):
        self.derivative = derivative

    def calc_derivative_at_point(self, point):
        return self.derivative(point[0])

    def step_forward(self, point, step_size):
        new_tuple_start = point[0] + step_size
        new_tuple_end = point[1] + self.calc_derivative_at_point(point)*step_size
        return (new_tuple_start, new_tuple_end)

    def calc_estimated_points(self, point, step_size, num_steps):
        estimated_list = [point]
        new_point = point
        for i in range(num_steps):
            new_point = self.step_forward(new_point, step_size)
            estimated_list.append(new_point)
        return estimated_list
