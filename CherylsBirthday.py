#When is Cheryl's Birthday?

DATES = ['May 15',    'May 16',    'May 19',
'June 17',   'June 18',
'July 14',   'July 16',
'August 14', 'August 15', 'August 17']

def Month(date):
    return date.split()[0]

def Day(date):
    return date.split()[1]

print('test Month(15):{}'.format(Month('May 15')))

def cheryl_birthday():
    return list(filter(state3to5,DATES))
    state3to5=all(state3 and state4 and state5)

#Albert: I don't know when Cheryl's birthday is, but I know that Bernard does not know too.
def state3(date):
    pass
