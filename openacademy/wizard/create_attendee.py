# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models

class createattendeewizard(models.TransientModel):
    _name='openacademy.create.attendee.wizard'

    @api.one
    def action_add_attendee(self):
        attendee_obj=self.env['openacademy.attendee']
        for wizard in self:
            for session in wizard.session_ids:
                for attendee in wizard.attendee_ids:
                    attendee_obj.create({'partner_id':attendee.partner_id.id, 'session_id':session.id})
        return {}

    @api.one
    def _get_sessions(self):
        print self._context
        ctx=dict(self._context)
        if ctx.get('active_model', '')== 'openacademy.session':
        	return ctx.get('active_ids', [])
        return []


    session_ids = fields.Many2many('openacademy.session', 'wizard_session_rel', 'wizard_id', 'session_ids', string='Sesiones', default=_get_sessions)
    attendee_ids = fields.One2many('openacademy.attendee.wizard', 'wizard_id', 'Asistentes')



class attendeewizard(models.TransientModel):
    _name='openacademy.attendee.wizard'

    _rec_name='partner_id'

    partner_id = fields.Many2one('res.partner', 'Asistente')
    wizard_id = fields.Many2one('openacademy.create.attendee.wizard', 'Wizard')
