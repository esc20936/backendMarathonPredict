def formatTime(decimal_time: float) -> str:
    hours = int(decimal_time)  
    minutes = round((decimal_time - hours) * 60)  
    
    return f"{hours} hours {minutes} minutes"
