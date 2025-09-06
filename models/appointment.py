from odoo import models, fields, api
from datetime import timedelta

class Appointment(models.Model):
    _name = 'healthcare.appointment'
    _description = 'Appointment'

    patient_id = fields.Many2one('healthcare.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('healthcare.doctor', string='Doctor', required=True)
    appointment_date = fields.Date(string='Appointment Date', required=True)

    start_time = fields.Float(string="Start Time (HH:MM)", required=True,
                              help="Time in hours (e.g. 14.5 = 14:30)")
    duration = fields.Float(string="Duration (hours)", required=True, default=1.0)
    end_time = fields.Float(string="End Time", compute="_compute_end_time", store=True)

    mode = fields.Selection([
        ('phone', 'Phone'),
        ('video', 'Video'),
        ('audio', 'Audio')
    ], string="Mode", required=True, default='phone')

    reason = fields.Char(string="Reason for Appointment")
    notes = fields.Text(string="Notes")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    @api.depends('start_time', 'duration')
    def _compute_end_time(self):
        for rec in self:
            if rec.start_time and rec.duration:
                rec.end_time = rec.start_time + rec.duration
            else:
                rec.end_time = rec.start_time
