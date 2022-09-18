import calendar
import time

ENDOFDAY = (24.0)
STARTOFDAY = (0, 0)
from plan import Plan


def get_date():
    timelst = time.localtime(time.time())
    return (timelst[0],timelst[1],timelst[2])

def get_weekdates():
    return [12, 13, 14, 15, 16, 17, 18]   # TODO start with monday  (cld.monthdayscalendar)

class Activity():

    def __init__(self, storage_file= "./data/data.txt"):
        self.plans = []
        self.storage_file = storage_file

        date = get_date()
        self.days_in_month = calendar.monthrange(date[0], date[1])[1]
        self.daily_act = {i + 1: [] for i in range(self.days_in_month)}   # start with 1
        self.calc_daily_act()


    # TODO


    def calc_daily_act(self):
        for i in self.plans:
            for j in i.periods:
                if (j[0])[0]==j[1][0] and (j[0])[1]==j[1][1]:
                    if (not i.isreminder) and (not i.isdeadline):
                        if (j[0])[2] == (j[1])[2]:
                            self.daily_act[(j[0])[2]].append((i, (((j[0])[3], (j[0])[4]), ((j[1])[3], (j[1])[4]))))  # daily_act value :(plan, time slot each day)
                        else:
                            for k in range((j[0])[2], (j[1])[2]):
                                self.daily_act[k].append((i, (((j[0])[3], (j[0])[4]), ENDOFDAY)))
                            self.daily_act[(j[1])[2]].append((i, (STARTOFDAY, ((j[1])[3], (j[1])[4]))))
                    else:
                        pass
                        # TODO
        return None

    def create(self, plan):
        self.plans.append(plan)
        self.calc_daily_act()

    def edit(self, index, newplan):
        self.plans[index] = newplan
        self.calc_daily_act()

    def refresh(self):
        pass

# def main():
#     act = Activity()
#     plan1 = Plan("p", periods=[((2022,9,17,15,0),(2022,9,17,17,0))])
#     plan2 = Plan("p", periods=[((2022, 9, 17, 18, 0), (2022, 9, 17, 20, 30)),((2022, 9, 18, 5, 0), (2022, 9, 19, 19, 0))])
#     act.create(plan1)
#     act.create(plan2)
#     print(act.daily_act)
#
# if __name__ == '__main__':
#     main()
def sis_api():
    pass #TODO