def calculate_aqi_pm25(pm25):
    if pm25 <= 30:
        return 50
    elif pm25 <= 60:
        return 100
    elif pm25 <= 90:
        return 200
    elif pm25 <= 120:
        return 300
    elif pm25 <= 250:
        return 400
    else:
        return 500


def calculate_aqi_pm10(pm10):
    if pm10 <= 50:
        return 50
    elif pm10 <= 100:
        return 100
    elif pm10 <= 250:
        return 200
    elif pm10 <= 350:
        return 300
    elif pm10 <= 430:
        return 400
    else:
        return 500


def overall_aqi(pm25, pm10):
    aqi_pm25 = calculate_aqi_pm25(pm25)
    aqi_pm10 = calculate_aqi_pm10(pm10)
    return max(aqi_pm25, aqi_pm10)
