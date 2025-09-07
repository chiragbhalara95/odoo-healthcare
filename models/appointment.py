from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class Appointment(models.Model):
    _name = 'healthcare.appointment'
    _description = 'Appointment'

    patient_id = fields.Many2one('healthcare.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('healthcare.doctor', string='Doctor', required=True)
    appointment_date = fields.Date(string='Appointment Date', required=True)

    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time", compute="_compute_end_time", store=True)
    duration = fields.Selection(
        [(str(i), f"{i} min") for i in range(5, 65, 5)],
        string="Duration",
        required=True,
        default="30"
    )

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

    name = fields.Char(string="Appointment Name", compute="_compute_name", store=True)

    @api.depends('patient_id', 'doctor_id')
    def _compute_name(self):
        for rec in self:
            if rec.patient_id:
                patient_name = f"{rec.patient_id.first_name} {rec.patient_id.last_name}"
            else:
                patient_name = "Unknown Patient"

            doctor_name = rec.doctor_id.name if rec.doctor_id else "Unknown Doctor"

            rec.name = f"{patient_name} with {doctor_name}"

    @api.depends('start_time', 'duration')
    def _compute_end_time(self):
        for rec in self:
            if rec.start_time and rec.duration:
                rec.end_time = rec.start_time + timedelta(minutes=int(rec.duration))
            else:
                rec.end_time = rec.start_time

    @api.constrains('start_time')
    def _check_start_time(self):
        for rec in self:
            if rec.start_time:
                hour = rec.start_time.hour
                # if hour < 9 or hour >= 19:
                #     raise ValidationError("Start time must be between 9:00 AM and 7:00 PM")
