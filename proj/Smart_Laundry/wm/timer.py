import datetime


def laundry_timer(hr, m, s):
    now = datetime.datetime.now().time().replace(microsecond=0)
    reservation = datetime.time(hr, m, s)

    while True:
        remaining_hours = reservation.hour - now.hour
        remaining_minutes = reservation.minute - now.minute
        remaining_seconds = reservation.second - now.second

        if reservation.hour >= now.hour:
            if reservation.minute >= now.minute:
                remaining_minutes = reservation.minute - now.minute
            else:
                remaining_hours -= 1
                remaining_minutes = reservation.minute - now.minute + 60

            if reservation.second >= now.second:
                remaining_seconds = reservation.second - now.second
            else:
                remaining_minutes -= 1
                remaining_seconds = reservation.second - now.second + 60

        return remaining_hours, remaining_minutes, remaining_seconds