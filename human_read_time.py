def format_duration(seconds):
    if seconds == 0: return 'now'
    
    second = 1
    minute = 60 * second
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day
    
    leftover = seconds
    output = []
        
    def fit(measurement, name, leftover):
        out = leftover / measurement
        if int(out) > 0:
            out = int(out)
            leftover -= out * measurement
            if out > 1:
                end = 's'
            else:
                end = ''
            output.append(str(out) + ' ' + name + end)
        return leftover
              
    leftover = fit(year, 'year', leftover)
    leftover = fit(day, 'day', leftover)
    leftover = fit(hour, 'hour', leftover)
    leftover = fit(minute, 'minute', leftover)
    leftover = fit(second, 'second', leftover)
    
    if len(output) > 1:
        out = ', '.join(output[:-1]) + ' and ' + output[-1]
    else:
        out = output[0]
    return out

