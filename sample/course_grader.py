# TODO-1: add convert_to_letter_grade(score) function
def convert_to_letter_grade(score):
    """Converts a numerical grade into a letter grade and returns a string containing the result
    
    Args: 
        score (int): The students current grade in the class.
        
    Returns:
        str: The letter grade corresponding to the students score.
        
    Raises:
        TypeError: If 'score' is not of type int.
        ValueError: If 'score' is less than zero, or greater than one hundred.
    """

    if not (isinstance(score, int)):
        raise TypeError("Score must be a numeric value.")
    elif (score < 0 or score > 100):
        raise ValueError("Score must be between 0 and 100.")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F" 