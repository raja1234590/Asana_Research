from datetime import datetime, timedelta


def weekday_biased_timestamp(offset_days=0):
    base = datetime.now() - timedelta(days=offset_days)
    while base.weekday() > 2: 
        base -= timedelta(days=1)
    return base
