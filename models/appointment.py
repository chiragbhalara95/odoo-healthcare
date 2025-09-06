from odoo import models, fields

class Appointment(models.Model):
    _name = 'healthcare.appointment'
    _description = 'Appointment'

    patient_id = fields.Many2one('healthcare.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('healthcare.doctor', string='Doctor', required=True)
    appointment_date = fields.Datetime(string='Date & Time', required=True)
    state = fields.Selection([
        ('draft','Draft'),
        ('confirmed','Confirmed'),
        ('done','Done'),
        ('cancelled','Cancelled')
    ], string='Status', default='draft')
    notes = fields.Text(string='Notes')
