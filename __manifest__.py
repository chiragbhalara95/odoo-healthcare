{
    'name': 'Healthcare Management',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Manage Patients, Doctors, and Appointments',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/appointment_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
}
