class Plan:

    def __init__(self, name, annotate=None, periods=None,
                 repeat=-1, isreminder=False, isdeadline=False):  # period should be [((year,month, day, hour, minute),(year,month, day, hour, minute))], 1 for perday, 2 for per week, 3 per month
        self.periods = periods
        self.name = name
        self.annotate = annotate
        self.reqeat = repeat
        self.isreminder = isreminder
        self.isdeadline = isdeadline
