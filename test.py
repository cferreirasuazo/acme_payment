import unittest
import datetime
from main import convertStringToDatetime, get_info, getDayPayment, get_payout_string, isValidFormat
from main import isValidRecordFormat, convertStringToDatetime, getPaymentRecords, calculateDifferenceInHour
from custom_exceptions import InvalidDayPaymentFormatError, InvalidRecordFormatError

class TestExtractInfo(unittest.TestCase):
    def test_get_name1(self):
        string = "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
        self.assertEqual(get_info(string, "name"), "ASTRID")

    def test_get_name2(self):
        string = "STEVEN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
        self.assertEqual(get_info(string, "name"), "STEVEN")

    def test_get_days1(self):
        string = "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
        self.assertEqual(get_info(string, "days"),
                         "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")

    def test_get_days2(self):
        string = "STEVEN=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
        self.assertEqual(get_info(string, "days"),
                         "MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")

class TestIsValidRecordFormat(unittest.TestCase):    
    def test_is_valid_record_format1(self):
         record_string = "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
         self.assertEqual(isValidRecordFormat(record_string),True)
    def test_is_valid_record_format2(self):
         record_string = "sdgdfgdsfgsdfgsdfgsdfgsdfgdfsgsdfgsdfgfdg" 
         self.assertEqual(isValidRecordFormat(record_string),False)
    def test_is_valid_record_format3(self):
         record_string = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00" 
         self.assertEqual(isValidRecordFormat(record_string),True)
    def test_is_valid_record_format4(self):
         record_string = "ASTRIDMO10:00-12:00,TH12:00-14:00,SU20:00-21:00" 
         self.assertEqual(isValidRecordFormat(record_string),False)
    def test_is_valid_record_format5(self):
         record_string = "ASTRID12345=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00" 
         self.assertEqual(isValidRecordFormat(record_string),False)
    def test_is_valid_record_format6(self):
         record_string = "ANAKIN=SU22:00-23:34,SA14:00-15:25,SA15:00-18:38,SA03:09-5:00,MO22:00-0:00,MO12:00-13:00,MO03:09-5:00" 
         self.assertEqual(isValidRecordFormat(record_string),True)

class TestRaiseException(unittest.TestCase):
    def test_raise_exception_invalid_day_payment_format_error1(self):
        self.assertRaises(InvalidDayPaymentFormatError, getDayPayment, "qwerty")

    def test_raise_exception_invalid_day_payment_format_error2(self):
        self.assertRaises(InvalidDayPaymentFormatError, getDayPayment, "M10:0-D0:000")

    def test_raise_exception_invalid_day_payment_format_error3(self):
        self.assertRaises(InvalidDayPaymentFormatError, getDayPayment, "")

    def test_out_of_range(self):
        self.assertRaises(Exception,getDayPayment, "SA15:00-18:38")

class TestCalculateDifferenceInHour(unittest.TestCase):
    def test_calculate_difference_in_hour1(self):
        time_a = datetime.time(19,0,0)
        time_b = datetime.time(0,0,0)
        self.assertEqual(calculateDifferenceInHour(time_a, time_b),5)
    def test_calculate_difference_in_hour2(self):
        time_a = datetime.time(10,0,0)
        time_b = datetime.time(12,0,0)
        self.assertEqual(calculateDifferenceInHour(time_a, time_b),2)
    def test_calculate_difference_in_hour3(self):
        time_a = datetime.time(4,0,0)
        time_b = datetime.time(0,0,0)
        self.assertEqual(calculateDifferenceInHour(time_a, time_b),20)
    def test_calculate_difference_in_hour4(self):
        time_a = datetime.time(10,0,0)
        time_b = datetime.time(14,0,0)
        self.assertEqual(calculateDifferenceInHour(time_a, time_b),4)
    def test_calculate_difference_in_hour5(self):
        time_a = datetime.time(10,30,0)
        time_b = datetime.time(11,0,0)
        self.assertEqual(calculateDifferenceInHour(time_a, time_b),0.5)





class TestConvertStringToDatetime(unittest.TestCase):
    def test_convert_to_datetime1(self):
        timestring = "01:13"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(1,13,0))
    def test_convert_to_datetime2(self):
        timestring = "01:15"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(1,15,0))
    def test_convert_to_datetime3(self):
        timestring = "03:16"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(3,16,0))
    def test_convert_to_datetime4(self):
        timestring = "03:09"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(3,9,0))
    def test_convert_to_datetime5(self):
        timestring = "07:25"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(7,25,0))
    def test_convert_to_datetime6(self):
        timestring = "18:00"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(18,0,0))
    def test_convert_to_datetime7(self):
        timestring = "22:00"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(22,0,0))
    def test_convert_to_datetime8(self):
        timestring = "18:00"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(18,0,0))
    def test_convert_to_datetime9(self):
        timestring = "05:01"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(5,1,0))
    def test_convert_to_datetime10(self):
        timestring = "22:00"
        self.assertEqual(convertStringToDatetime(timestring), datetime.time(22,0,0))

class TestIsValidFormat(unittest.TestCase):

    def test_isValidFormat1(self):
        payment_day_str = "MO10:00-12:00"
        self.assertTrue(isValidFormat(payment_day_str))

    def test_isValidFormat2(self):
        payment_day_str = "TU10:00-x:00"
        self.assertFalse(isValidFormat(payment_day_str))

    def test_isValidFormat3(self):
        payment_day_str = "TH01:00-03:00"
        self.assertTrue(isValidFormat(payment_day_str))

    def test_isValidFormat4(self):
        payment_day_str = "SA1400-18:00"
        self.assertFalse(isValidFormat(payment_day_str))
        
    def test_isValidFormat5(self):
        payment_day_str = "SU20:00-21:00"
        self.assertTrue(isValidFormat(payment_day_str))

    def test_isValidFormat6(self):
        payment_day_str = "MO10:00-12:0"
        self.assertFalse(isValidFormat(payment_day_str))

    def test_isValidFormat7(self):
        payment_day_str = "TH12:00-14:00"
        self.assertTrue(isValidFormat(payment_day_str))
    
    def test_isValidFormat8(self):
        payment_day_str = "SU20:00-21:00"
        self.assertTrue(isValidFormat(payment_day_str))

class TestPayOutString(unittest.TestCase):
    def test_payout_string1(self):
        self.assertEqual(get_payout_string("RENE", 215),"The amount to pay RENE is: 215 USD")

    def test_payout_string2(self):
        self.assertEqual(get_payout_string("ASTRID", 85),"The amount to pay ASTRID is: 85 USD")

if __name__ == '__main__':
    unittest.main()
