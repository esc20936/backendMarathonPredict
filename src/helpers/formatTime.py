def formatTime(decimal_time: float) -> str:
    hours = int(decimal_time)  
    minutes = round((decimal_time - hours) * 60)  
    
    return f"{hours} hours {minutes} minutes"

def formatTime2(decimal_time: float) -> str:
    hours = int(decimal_time // 3600)  # Get the number of full hours
    minutes = int((decimal_time % 3600) // 60)  # Get the remaining minutes

    return f"{hours} hours {minutes} minutes"
