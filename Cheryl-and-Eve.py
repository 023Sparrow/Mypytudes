# Albert and Bernard just became friends with Cheryl, and they want to know when her birthday is.
# Cheryl gives them a set of 10 possible dates:

cheryl_dates = DATES = {
    'May 15',    'May 16',    'May 19',
    'June 17',   'June 18',
    'July 14',   'July 16',
    'August 14', 'August 15', 'August 17'}


def month(date): return date.split()[0]


def day(date): return date.split()[1]

# Cheryl then tells Albert and Bernard separately
# the month and the day of the birthday respectively.


def tell(part):
    "Cheryl tells a part of her birthdate; return a subset of DATES that match the part."
    return {date for date in DATES if part in date}


def know(possible_dates):
    "A person knows the birthdate if they know there is exactly one possible date."
    return len(possible_dates) == 1


def hear(possible_dates, *statements):
    "Return the subset of possible dates that are consistent with all the statements."
    return {date for date in possible_dates
            if all(stmt(date) for stmt in statements)}

# Albert and Bernard make three statements:


def albert1(date):
    "Albert: I don't know when Cheryl's birthday is, but I know that Bernard does not know too."
    after_being_told = tell(month(date))
    return (not know(after_being_told)
            and all(not know(tell(day(d)))
                    for d in after_being_told))


def bernard1(date):
    "Bernard: At first I don't know when Cheryl's birthday is, but I know now."
    at_first = tell(day(date))
    return (not know(at_first)
            and know(hear(at_first, albert1)))


def albert2(date):
    "Albert: Then I also know when Cheryl's birthday is."
    return know(hear(tell(month(date)), bernard1))

# So when is Cheryl's birthday?


def cheryls_birthday(dates):
    "Return a list of the possible dates after hearing the three statements."
    return hear(using(dates), albert1, bernard1, albert2)


def using(dates):
    "Make dates be the value of the global variable DATES."
    global DATES  # This is necessary because `tell` looks at `DATES`
    DATES = dates
    return dates

# Some tests


assert month('May 19') == 'May'
assert day('May 19') == '19'
assert albert1('May 19') == False
assert albert1('July 14') == True
assert know(tell('17')) == False
assert know(tell('19')) == True

cheryls_birthday(cheryl_dates)
