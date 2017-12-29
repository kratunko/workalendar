# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
from workalendar.core import WesternCalendar, OrthodoxMixin
from workalendar.registry import iso_register


@iso_register('MD')
class Moldova(OrthodoxMixin, WesternCalendar):
    name = 'Moldova'

    FIXED_HOLIDAYS = WesternCalendar.FIXED_HOLIDAYS + (
        (1, 2, "New Year - 2nd day"),
        (1, 7, "Orthodox Christmas Day"),
        (1, 8, "Orthodox Christmas Day holiday"),
        (3, 8, "International Women's Day"),
        (4, 16, "Orthodox Easter Sunday"),
        (4, 17, "Orthodox Easter Monday"),
        (4, 24, "Memorial Day/Parents' Day"),
        (5, 1, "International Day of Solidarity of Workers"),
        (5, 8, "Victory Day (Bridge Holiday)"),
        (5, 9, "Victory Day"),
        (6, 2, "Chrildren's Day Extra Holiday"),
        (8, 27, "Independence Day"),
        (8, 28, "Independence Day Holiday"),
        (8, 31, "Language Day"),
        (9, 1, "Language Day Extra Holiday"),
    )

    include_good_friday = False
    include_easter_sunday = False
    include_easter_monday = False
    include_whit_sunday = False
    whit_sunday_label = 'Pentecost'
    include_whit_monday = False

    include_christmas = True
    include_boxing_day = False
    boxing_day_label = 'Christmas Day'

    def get_childrens_day(self, year):
        """returns a possibly empty list of (date, holiday_name) tuples"""
        days = []
        if year >= 2017:
            actual_date = date(year, 6, 1)
            days = [(actual_date, "Children's Day")]

        return days

    def get_liberation_day(self, year):
        """returns a possibly empty list of (date, holiday_name) tuples"""
        days = []
        if year >= 1949 and year <= 1990:
            actual_date = date(year, 8, 23)
            days = [(actual_date, "Liberation from Fascist Occupation Day")]

        return days

    def get_variable_days(self, year):
        days = super(Moldova, self).get_variable_days(year)
        days.extend(self.get_childrens_day(year))
        days.extend(self.get_liberation_day(year))
        return days
