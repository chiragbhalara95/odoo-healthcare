from odoo import models, fields


class Patient(models.Model):
    _name = 'healthcare.patient'
    _description = 'Patient'

    # ------------------------
    # Basic Identity
    # ------------------------
    title = fields.Selection(
        [
            ('mr', 'Mr.'),
            ('ms', 'Ms.'),
            ('mrs', 'Mrs.'),
            ('dr', 'Dr.')
        ],
        string="Title"
    )
    first_name = fields.Char(string="First Name", required=True)
    middle_name = fields.Char(string="Middle Name")
    last_name = fields.Char(string="Last Name")
    suffix = fields.Selection(
        [
            ('sr', 'Sr.'),
            ('jr', 'Jr.'),
            ('i', 'I'),
            ('ii', 'II'),
            ('iii', 'III')
        ],
        string="Suffix"
    )

    dob = fields.Date(string="Date of Birth")
    gender = fields.Selection(
        [
            ('male', 'Male'),
            ('female', 'Female'),
            ('other', 'Other')
        ],
        string="Gender"
    )
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    medical_history = fields.Text(string="Medical History")

    # ------------------------
    # Languages
    # ------------------------
    spoken_language = fields.Selection(
        [
            ('en', 'English'),
            ('fr', 'French'),
            ('es', 'Spanish'),
            ('hi', 'Hindi'),
            ('gu', 'Gujarati'),
            ('other', 'Other')
        ],
        string="Spoken Language"
    )
    official_language = fields.Selection(
        [
            ('en', 'English'),
            ('fr', 'French'),
            ('es', 'Spanish'),
            ('hi', 'Hindi'),
            ('gu', 'Gujarati'),
            ('other', 'Other')
        ],
        string="Official Language"
    )

    # ------------------------
    # Residential Address
    # ------------------------
    street = fields.Char(string="Street")
    city = fields.Char(string="City")
    province = fields.Char(string="Province/State")
    postal_code = fields.Char(string="Postal Code")

    # ------------------------
    # Mailing Address
    # ------------------------
    is_same_address = fields.Boolean(
        string="Mailing Address same as Residential?",
        default=True
    )
    mailing_street = fields.Char(string="Mailing Street")
    mailing_city = fields.Char(string="Mailing City")
    mailing_province = fields.Char(string="Mailing Province/State")
    mailing_postal_code = fields.Char(string="Mailing Postal Code")

    # ------------------------
    # Alternative Contact
    # ------------------------
    alt_first_name = fields.Char(string="Alt. First Name")
    alt_last_name = fields.Char(string="Alt. Last Name")
    alt_contact_number = fields.Char(string="Alt. Contact Number")
    alt_email = fields.Char(string="Alt. Email")
    alt_relationship = fields.Selection(
        [
            ('parent', 'Parent'),
            ('spouse', 'Spouse'),
            ('sibling', 'Sibling'),
            ('friend', 'Friend'),
            ('guardian', 'Guardian'),
            ('other', 'Other')
        ],
        string="Relationship with Patient"
    )
    alt_note = fields.Text(string="Alt. Contact Notes")
