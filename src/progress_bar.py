from time import time


class ProgressBar:

    def __init__(self, total, length, task):
        self.iteration = 0
        self.total = total
        self.length = length
        self.task = task
        self.started, self.finished = time(), int()

    def update(self):
        percent = "{0:.f}".format(100 * (self.iteration / float(self.total)))
        filledLength = int(self.length * self.iteration // self.total)
        bar = "=" * filledLength + "-" * (self.length - filledLength)
        print("\r%s |%s¬ %s%% %s" % ("Progress", bar, percent, "Complete"), end='\r')
        print(f"Objective: {self.task}")

        # Print finished.
        if self.iteration == self.total:
            self.finished = time()
            print(f"Finished in: {self.finished - self.started}")
