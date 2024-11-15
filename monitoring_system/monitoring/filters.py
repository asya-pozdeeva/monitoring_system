class MovingAverager:
    """Скользащее среднее"""
    def __init__(self, N):
        self.N = N
        self.alpha = 2 / (1 + N)
        self.ema_prev = None
    def filter_value(self, value):
        if self.ema_prev is None:
            self.ema_prev = value
        else:
            self.ema_prev = (value * self.alpha) + (self.ema_prev * (1 - self.alpha))
        return self.ema_prev