import tkinter


class Counter:  
    def __init__(self, sec, timeLabel, master):
        self.sec = sec
        self.timeLabel = timeLabel
        self.doTick = False
        self.master = master
        self.tick()

    def tick(self):
        if not self.doTick:
            return
        if self.sec == 1:
            self.doTick = False
        self.sec -= 1
        self.timeLabel.configure(text=self.sec)
        self.master.after(1000, self.tick)

    def start(self):
        self.doTick = True
        self.tick()

    def stop(self):
        self.doTick = False

    def resume(self):
        self.doTick = True
        self.tick()
    
    def reset(self,sec):
        self.doTick = True
        self.sec = sec
        self.timeLabel.configure(text=self.sec)