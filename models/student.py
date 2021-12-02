#-*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityStudent(models.Model):
     _name = 'university.student'

     f_name = fields.Char('First name')
     l_name = fields.Char('Last name')
     sexe =  fields.Selection([('male','Male'),('female','Female')])
     identity_card = fields.Char('Identity card')
     address = fields.Text('Address')
     birthday = fields.Date('Birthday')
     registration_date = fields.Date('Registration Date')
     email = fields.Char()
     phone = fields.Char()

     department_id = fields.Many2one(comodel_name='university.department')
     classroom_id = fields.Many2one(comodel_name='university.classroom')

     subject_ids = fields.Many2many(related='classroom_id.subject_ids')

     @api.multi
     def name_get(self):
          result = []
          for student in self:
               name = '[' + str(student.classroom_id.classroom_name) + '] ' + student.f_name + ' ' + student.l_name
               result.append((student.id, name))

          return result

     @api.one
     @api.constrains('registration_date','birthday')
     def check_dates(self):
          if self.birthday > self.registration_date:
               raise ValueError('The birthday must be inferior than the registration date')
