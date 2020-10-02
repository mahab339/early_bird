from odoo import models, fields, api 
 
class Attendance(models.Model): 
    _name = 'early_bird.attendance' 
    _description = "Attendance records" 
     
    user_id = fields.Many2one('res.users') 
    arrival = fields.Datetime(string='Arrival time')
    leave = fields.Datetime(string='Leave time')
