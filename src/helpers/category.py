def categorize_time(decimal_time: float) -> str:
    if decimal_time < 3:
        return "Expert"
    elif 3 <= decimal_time < 3.33:  
        return "Advanced"
    elif 3.33 <= decimal_time < 3.67:  
        return "Intermediate"
    elif 3.67 <= decimal_time < 4:
        return "Beginner"
    else:
        return "Noob"