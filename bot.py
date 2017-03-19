from cali_condemned_inmates import birthday_message
from weather import weather_message



#take's user's birthday as a four-digit day/month string (e.g. "01/13" for January 13)
def bot(birthday):

    birthday = birthday_message(birthday)

    weather = weather_message(birthday)

    message = birthday + weather

    return message

    """

    On your next birthday, {inmate_name} will have been on death row for {yrs_since_sentence}.
    There was a high of {high_temp} degrees fahrenheit, and a low of {low_temp} in {trial_county},
    where {inmate_last_name} committed their crime on {offense_date}.

    """