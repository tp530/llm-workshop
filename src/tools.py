import random

def get_current_wait_time(hospital: str) -> int | str:
    """An example function to generate wait times"""

    hospitals = [
        "Wallace-Hamilton",
        "Burke, Griffin and Cooper",
        "Walton LLC",
        "Garcia Ltd"
    ]

    if hospital not in hospitals:
        return f"Hospital {hospital} does not exist."

    return random.randint(10, 100)
