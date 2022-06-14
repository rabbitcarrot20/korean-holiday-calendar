===============
korean_holiday_calendar
===============

This is a Korean-specialized version of python-holidays package (by dr-prodigy), which contains key functions in existing package, and some new functions for calculating and analysing Korean holidays.

The usage is mostly the same as the existing python-holidays package, so please read its instruction manual for a more complicated usage.

https://python-holidays.readthedocs.io/

Below is a brief instruction manual based on our package.


Quick Start
-----------

.. code-block:: python

    from datetime import date
    import kr_holidays

    kr = krholidays.KR()  # this is a dict
    # the below is the same, but takes a string:
    kr = krholidays.country_holidays('KR')  # this is a dict

    date(2015, 1, 1) in kr_holidays  # True
    date(2015, 1, 2) in kr_holidays  # False
    kr_holidays.get('2014-01-01')  # "신정"
    
For English users, we added English options.

.. code-block:: python

    kr_holidays_en = holidays.KR(en_name = True)
    
    kr_holidays_en.get('2014-01-01')  # "New Year's Day"

The 'HolidayBase', a dict-like class, will also recognize date strings and Unix
timestamps:

.. code-block:: python

    '2014-01-01' in kr_holidays  # True
    '1/1/2014' in kr_holidays    # True
    1388597445 in kr_holidays    # True



Manuals
-------

Example usage:

.. code-block:: python

    from krholidays import country_holidays
    kr = country_holidays('KR')
    
The below will cause 2015 holidays to be calculated on the fly:

.. code-block:: python

    from datetime import date
    date(2015, 1, 1) in kr  # True
    

The :class:`HolidayBase` class also recognizes strings of many formats
and numbers representing a POSIX timestamp:

>>> assert '2014-01-01' in kr
>>> assert '1/1/2014' in kr
>>> assert 1388597445 in kr

Show the holiday's name:

.. code-block:: python

    kr.get('2014-01-01')   #"New Year's Day"

Check a range:

.. code-block:: python

    kr['2014-01-01': '2014-01-03']   #[datetime.date(2014, 1, 1)]

List all 2020 holidays:

.. code-block:: python

    kr_2020 = country_holidays('KR', years=2020)
    for day in kr_2020.items():
         print(day)
    
    #
    (datetime.date(2020, 1, 1), '신정')
    (datetime.date(2020, 1, 24), '설날 연휴')
    (datetime.date(2020, 1, 25), '설날')
    (datetime.date(2020, 1, 26), '설날 연휴')
    (datetime.date(2020, 1, 27), '설날 대체공휴일')
    (datetime.date(2020, 3, 1), '3·1절')
    (datetime.date(2020, 4, 30), '부처님오신날')
    (datetime.date(2020, 5, 5), '어린이날')
    (datetime.date(2020, 6, 6), '현충일')
    (datetime.date(2020, 8, 15), '광복절')
    (datetime.date(2020, 10, 1), '추석')
    (datetime.date(2020, 10, 2), '추석 연휴')
    (datetime.date(2020, 9, 30), '추석 연휴')
    (datetime.date(2020, 10, 3), '개천절')
    (datetime.date(2020, 10, 9), '한글날')
    (datetime.date(2020, 12, 25), '기독탄신일')
    (datetime.date(2020, 4, 15), '제21대 국회의원 선거일')
    (datetime.date(2020, 8, 17), '광복절 기념 (임시공휴일)')
   

Append custom holiday dates by passing one of:

* a :class:`dict` with date/name key/value pairs (e.g. {'2010-07-10': 'My birthday!'}),
* a list of dates (as a :class:`datetime.date`, :class:`datetime.datetime`, 
:class:`str`, :class:`int`, or :class:`float`); ``'Holiday'`` will be used as a description,
* or a single date item (of one of the types above);


.. code-block:: python

    custom_holidays = country_holidays('US', years=2015)
    custom_holidays.update({'2015-01-01': "New Year's Day"})
    custom_holidays.update(['2015-07-01', '07/04/2015'])
    custom_holidays.update(date(2015, 12, 25))
    
Newly added functions : import them as you want.

* count_sun(year), count_sat(year) : Count the number of Sundays / Saturdays for the year.

* count_holidays(base, year, include_sun = False, include_sat = False) : Count the number of holidays, which add or disable Saturdays and Sundays as you specify.
* 'base' is 'a HolidayBase object that predetermined in years'.
 
* years_graph(start, end, sat = False, sun = False) : Draw a matplotlib.pyplot barplot of the number of holidays between specified year term. You can include Saturday and Sunday options like as count_holidays.

* months_graph(year) : Draw a matplotlib.pyplot barplot of the number of holidays per month, in a specified year.
    
    
License
-------

.. __: LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).