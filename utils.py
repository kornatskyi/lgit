import datetime


def generate_folder_name_from_date(date: datetime.datetime):
    return date.strftime('%S') + date.strftime('%M') + date.strftime('%H') + date.strftime('%d') + date.strftime('%m') + date.strftime('%Y')
