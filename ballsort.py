class Rack:

    def __init__(self):
        self.balls = []

    def add(self, ball):
        self.balls.append(ball)
        self.bubble_sort(self.balls)

    def bubble_sort(self, balls):
        while not self.is_sorted(balls):
            self.balls = self.bubble(balls)

    def is_sorted(self, balls):
        for ball, next in zip(balls, balls[1:]):
            if ball > next:
                return False
        return True

    def bubble(self, balls):
        for i in range(1, len(balls)):
            if balls[i - 1] > balls[i]:
                balls[i - 1], balls[i] = balls[i], balls[i - 1]
        return balls



