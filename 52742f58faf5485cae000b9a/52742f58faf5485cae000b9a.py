def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        duration_value ={"year": 31536000,
                     "day": 86400,
                     "hour": 3600,
                     "minute": 60,
                     "second": 1}
        result = ""
        for key, value in duration_value.items():
            if value <= seconds:
                if len(result)> 0:
                    result +=  ", "
                time = int(seconds/value)
                result += f"{time} {key}s" if time > 1 else f"{time} {key}"
                seconds = seconds%value
        temp =result.split(", ")
        if len(temp) > 1:
            result = ", ".join(temp[:-1]) + " and " + temp[-1]
        return result