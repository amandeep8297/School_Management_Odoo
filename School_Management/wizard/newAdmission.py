from odoo import fields,models

class NewAdmissionWizard(models.TransientModel):
    _name="admission.wizard"
    _description="New Admission Wizard"
    
    student_id=fields.Many2one('school.student',required=True)
    def action_create_admission(self):
        print("Button is clicked")