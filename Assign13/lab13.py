import time
class Clock:
    def __init__(self, hour, minute, second, clock_type=0):

        self.hour = hour

        self.minute = minute

        self.second = second

        self.clock_type = clock_type
    def __str__(self):

        if self.clock_type == 0:

            return (" {:02}".format(self.hour) + " : " + "{:02}".format(self.minute) + " : " + "{:02}".format(
                self.second))
        else:

            if self.hour >= 0 and self.hour <= 11:

                if self.hour == 0:

                    return (" 12 : " + "{:02}".format(self.minute) + " : " + "{:02}".format(self.second) + " am ")

                else:

                    return (" {:02}".format(self.hour) + " : " + "{:02}".format(self.minute) + " : " + "{:02}".format(
                        self.second) + " am")

            else:

                if self.hour == 12:

                    return (" {:02}".format(self.hour) + " : " + "{:02}".format(self.minute) + " : " + "{:02}".format(
                        self.second) + " pm")

                else:

                    mod_hour = self.hour - 12

                    return (" {:02}".format(mod_hour) + " : " + "{:02}".format(self.minute) + " : " + "{:02}".format(
                        self.second) + " pm")
    def tick(self):

        self.second = self.second + 1

        if self.second == 60:

            self.minute = self.minute + 1

            self.second = 0

            if self.minute == 60:

                self.hour = self.hour + 1

                self.minute = 0

                if self.hour == 24:
                    self.hour = 0

def main():
    hour = int(input(' What is the current hour ==> '))

    minute = int(input(' What is the current minute ==> '))

    second = int(input(' What is the current second ==> '))

    clock = Clock(hour, minute, second, 1)  # create a 12-hour clock

    while True:
        print(clock)

        clock.tick()

        time.sleep(1)

if __name__ == "__main__":
    main()