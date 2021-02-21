import random


def classify_timecard(hours_worked: float) -> str:
    """Classifies employee as part/full/over - time"""
    if hours_worked < 20:
        employment_status = "part time"
    elif 20 <= hours_worked <= 40:
        employment_status = "Full time"
    elif hours_worked >= hours_worked:
        employment_status = "Over time"
    return employment_status


def get_pay_rate() -> float:
    """returns pay rates based on set percentages"""
    a_number = random.randrange(5)
    if a_number <= 2:
        pay_rate = 12.35
    elif a_number == 3:
        pay_rate = 20.12
    elif a_number == 4:
        pay_rate = 38.56
    return pay_rate


def get_hours_worked() -> float:
    """Returns the number of hours worked based on
    the following percentages"""
    a_number = random.randrange(4)
    if a_number <= 1:  # random time between
        # 20.0 & 39.9, 50% of the time
        random_number = random.uniform(20.0, 39.9)
    elif a_number == 2:  # random time between
        # 10.0 & 34.9, 25% of the time
        random_number = random.uniform(10.0, 34.9)
    elif a_number == 3:  # random time between
        # 30.0 & 59.9, 25% of the time
        random_number = random.uniform(30.0, 59.9)
    random_number_format = float(format(random_number, ".1f"))
    return random_number_format


def is_in_range(test_value: int,
                min_value: int,
                max_value: int) -> bool:
    """returns True or False depending on parameters"""
    if min_value <= test_value <= max_value:
        bool_val = True
    else:
        bool_val = False
    return bool_val

