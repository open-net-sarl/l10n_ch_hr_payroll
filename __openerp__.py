# -*- coding: utf-8 -*-
#
#  File: __init__.py
#  Module: l10n_ch_hr_payroll
#
#  Created by sge@open-net.ch
#
#  Copyright (c) 2014-TODAY Open-Net Ltd. <http://www.open-net.ch>
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-TODAY OpenERP S.A. <http://www.openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Switzerland - Payroll',
    'category': 'Localization',
    'author': 'Open-Net Sàrl',
    'depends': ['hr_payroll'],
    'version': '0.0.5',
    'description': """
Swizerland Payroll Rules.
=========================

**Features list :**
    * Salary rule categories
    * Salary rules
    * Employee children in school
    * Contract LPP range

**Author :** Open Net Sàrl   Industrie 59  1030 Bussigny  Suisse  http://www.open-net.ch

**Contact :** info@open-net.ch

**History :**

V1.0: 2014-11-07/Sge
    * Add Salary rule categories
    * Add Salary rules
    * Add Employee children in school
    * Add Contract LPP range

    """,

    'auto_install': False,
    'demo': [],
    'website': 'http://open-net.ch',
    'data':[
        'hr_contract_view.xml',
        'hr_employee_view.xml',
        'l10n_be_hr_payroll_data.xml',
        'data/hr.salary.rule-change.csv',
        'data/hr.salary.rule-new.csv',
    ],
    'installable': True
}
