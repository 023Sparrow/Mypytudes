# When is Cheryl's Birthday?

DATES = ['May 15',    'May 16',    'May 19',
         'June 17',   'June 18',
         'July 14',   'July 16',
         'August 14', 'August 15', 'August 17']


def Month(date):
    # 返回月份字符串
    return date.split()[0]


def Day(date):
    # 返回天数字符串
    return date.split()[1]


def tell(part, possible_dates=DATES):
        # 返回由告知信息月或天可猜得的日期
    # return list(filter(lambda i: part in i, possible_dates))
    return [date for date in possible_dates if part in date]


def know(possible_dates):
    if len(possible_dates) == 1:
        return True


print(tell('May'))


def cheryl_birthday():
    return list(filter(state3to5, DATES))


def state3to5(date):
    return state3(date) and state4(date) and state5(date)


# Albert: I don't know when Cheryl's birthday is,
# but I know that Bernard does not know too.


def state3(date):
    possible_dates = tell(Month(date))
    if not know(possible_dates) and all([not know(tell(Day(date))) for date in possible_dates]):
        return True


# Bernard: At first I don't know when Cheryl's birthday is, but I know now.


def state4(date):
    at_first = tell(Day(date))
# 一开始猜测的日期，一定不止一个
    if not know(at_first) and know(list(filter(state3, at_first))):
        # 得知A的第一个陈述后猜测得唯一日期
        return True

# Albert: Then I also know when Cheryl's birthday is.


def state5(date):
    return know(list(filter(state4, tell(Month(date)))))
    # return know([item for item in list(filter(state4, filter(state3, DATES))) if Month(date) in item])


# print(list(filter(state5, (list(filter(state4, filter(state3, DATES)))))))


print(know(cheryl_birthday()))
