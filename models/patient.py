from odoo import models, fields

class Patient(models.Model):
    _name = 'healthcare.patient'
    _description = 'Patient'

    name = fields.Char(string='Name', required=True)
    dob = fields.Date(string='Date of Birth')
    gender = fields.Selection([('male','Male'), ('female','Female')], string='Gender')
    phone = fields.Char(string='Phone')
    medical_history = fields.Text(string='Medical History')
