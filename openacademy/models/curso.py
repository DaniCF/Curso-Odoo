# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models

class openacademy_course(models.Model):
	_name='openacademy.course'

	name = fields.Char('Nombre', required=True)
	description = fields.Text('Descripción')
	responsible_id = fields.Many2one("res.partner", "Responsable")
	session_ids = fields.One2many("openacademy.session","course_id", "Sesiones")


class openacademy_session(models.Model):
	__name='openacademy.session'

	name = fields.Char('Nombre', required=True)
	start_date = fields.Date('Fecha Inicio')
	duration = fields.Integer('Duracion')
	seats = fields.Integer("Num Asientos")
	instructor_id = fields.Many2one("res.partner", "Instructor")
	course_id = fields.Many2one("openacademy.course", "Cursos", ondelete="cascade")

class openacademy_attendee(models.Model):
	_name='openacademy.attendee'

	_rec_name='partner_id'

	partner_id = fields.Many2one("res.partner", "Asistente", ondelete="cascade")
	session_id = fields.Many2one("openacademy.session", "Sesion", ondelete="cascade")