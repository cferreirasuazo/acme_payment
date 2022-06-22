import re
import datetime
from custom_exceptions import InvalidDayPaymentFormatError, InvalidRecordFormatError
import math


def convertStringToDatetime(time_string):
    hour, minutes = [int(i) for i in time_string.split(":")]
    return datetime.time(hour, minutes, 0)


def isValidFormat(input):
    day_payment_regex = "^[a-zA-Z]+(0?[0-9]|1[0-9]|2[0-3]):[0-9]+-(0?[0-9]|1[0-9]|2[0-3]):[0-5][0-9]+$"
    pattern = re.compile(day_payment_regex, re.IGNORECASE)
    return pattern.match(input)


def isValidRecordFormat(input):
    payment_record_regex = "^[a-zA-z]+=.*"
    pattern = re.compile(payment_record_regex, re.IGNORECASE)
    if not pattern.match(input):
        return False
    return True


def isHoursInRange(start_hour, end_hour, employee_start_hour, employee_end_hour):
    midnight_plus_one = datetime.time(0, 1, 0)

    if (start_hour <= employee_start_hour <= end_hour) and (start_hour <= employee_end_hour <= end_hour):
        return True
    if end_hour < midnight_plus_one:
        if (start_hour <= employee_start_hour <= midnight_plus_one) and (start_hour <= employee_end_hour <= midnight_plus_one):
            return True
    return False


def getPaymentRecords(file_name):
    records = []
    with open(file_name) as file:
        for record in file:
            end = len(record) - 1
            record_string = record[0:end].strip()
            if not isValidRecordFormat(record_string):
                raise InvalidRecordFormatError(record_string)
            records.append(record_string)
    return records


def get_info(str, value):
    hash_values = {
        "name": 0,
        "days": 1
    }
    return str.split("=")[hash_values[value]]


def calculateDifferenceInHour(time_a, time_b):
    midnight = datetime.time(0, 0, 0)
    dateTimeA = datetime.timedelta(hours=time_a.hour, minutes=time_a.minute)
    dateTimeB = datetime.timedelta(hours=time_b.hour, minutes=time_b.minute)
    if time_b == midnight:
        dateTimeB = datetime.timedelta(hours=24, minutes=0)

    dateTimeDifference = dateTimeB - dateTimeA
    dateTimeDifferenceInHours = dateTimeDifference.total_seconds() / 3600
    diff = round(dateTimeDifferenceInHours, 1)
    return diff


def getDayPayment(payment_record):
    payment_record = payment_record.strip()
    weekdays = ["MO", "TU", "WE", "TH", "FR"]
    weekends = ["SA", "SU"]

    if isValidFormat(payment_record):
        day = payment_record[0:2]
        start_hour_string, end_hour_string = payment_record[2:-1].split("-")
        start_hour = convertStringToDatetime(start_hour_string)
        end_hour = convertStringToDatetime(end_hour_string)
        time_diff = calculateDifferenceInHour(start_hour, end_hour)
        start_1 = datetime.time(0, 1, 0)
        end_1 = datetime.time(9, 0, 0)
        start_2 = datetime.time(9, 1, 0)
        end_2 = datetime.time(18, 0, 0)
        start_3 = datetime.time(18, 1, 0)
        end_3 = datetime.time(23, 59, 0)
        if day in weekdays:
            if isHoursInRange(start_1, end_1, start_hour, end_hour):
                return 25 * time_diff
            elif isHoursInRange(start_2, end_2, start_hour, end_hour):
                return 15 * time_diff
            elif isHoursInRange(start_3, end_3, start_hour, end_hour):
                return 20 * time_diff
            else:
                raise Exception(f"Out of range {payment_record} ")

        elif day in weekends:
            if isHoursInRange(start_1, end_1, start_hour, end_hour):
                return 30 * time_diff
            elif isHoursInRange(start_2, end_2, start_hour, end_hour):
                return 20 * time_diff
            elif isHoursInRange(start_3, end_3, start_hour, end_hour):
                return 25 * time_diff
            else:
                raise Exception(f"Out of range {payment_record} ")
        else:
            raise Exception(f"Invalid day: {day}")

    else:
        raise InvalidDayPaymentFormatError(payment_record)


def get_payout_string(name, total):
    return f"The amount to pay {name} is: {total} USD"

def main():
    try:
        records = getPaymentRecords("payment_records.txt")
        for record in records:
            name = get_info(record, "name")
            days_payment = get_info(record, "days").split(",")
            total = sum([getDayPayment(payment_string)
                        for payment_string in days_payment])
            payout_string = get_payout_string(name, total)
            print(payout_string)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
