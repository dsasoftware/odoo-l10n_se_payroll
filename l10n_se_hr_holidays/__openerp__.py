# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2004-2016 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Swedish - Holidays',
    'category': 'Localization',
    'author': 'Vertel AB',
    'depends': ['hr_holidays_sequence','l10n_se_hr_payroll'],
    'version': '1.0',
    'licence': 'AGPL-3',
    'summary': 'Swedish Holidays Rules',
    'description': """
Swedish Holidays Rules
======================

* Add holidays earning rules to payroll (hr.holiday)
* Add hr.holiday.earning to hr.employee
* Add holiday year to hr.holiday

* hr.holiday.earning can be used for flextime and normal leaves days
* Holiday earning rules can add days to an employees hr.holidays.earning
  from hr.payslip


    """,
    'auto_install': False,
    'website': 'http://vertel.se',
    'data':[
        'hr_employee_view.xml',
        'hr_holidays_view.xml',
        'hr_holidays_data.xml',
        'hr_salary_rule_data_holiday.xml',
        'hr_payroll_payslip_report.xml',
        'hr_salary_rule_data_sick.xml',
    ],
    'demo':[
    ],
    'installable': True
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
