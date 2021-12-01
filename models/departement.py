from odoo import models, fields, api

class UniversityDepartementt(models.Model):
     _name = 'university.departement'

     name = fields.Char()
     code = fields.Char()