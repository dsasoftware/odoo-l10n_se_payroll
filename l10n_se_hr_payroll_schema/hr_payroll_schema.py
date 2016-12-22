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
from openerp import models, fields, api, _

import logging
_logger = logging.getLogger(__name__)

class hr_payroll_structure(models.Model):
    _inherit = 'hr.salary.structure'

    def init_records(self,cr,uid, context=None):
        hr_payroll_structure-gl = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'l10n_se_hr_payroll', 'hr_payroll_structure-gl')
        self.pool.get('hr.salary.structure').write(cr,uid,hr_payroll_structure-gl[1],{
            'rule_ids': [(4, ref('hr_salary_rule-schemajust'))],
        })
        hr_payroll_structure-tim = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'l10n_se_hr_payroll', 'hr_payroll_structure-tim')
        self.pool.get('hr.salary.structure').write(cr,uid,hr_payroll_structure-tim[1],{
            'rule_ids': [(4, ref('hr_salary_rule-schemahour')), (4, ref('hr_salary_rule-prej-tim'))],
        })

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
