from odoo import models, fields, api

class UniversityClassroom(models.Model):
     _name = 'university.classroom'
     _rec_name = 'classroom_name'

     classroom_name = fields.Char(string='name')
     code = fields.Char()

     student_ids = fields.One2many(comodel_name='university.student', inverse_name='classroom_id')

     professor_ids = fields.Many2many(comodel_name='university.professor',
                                      relation='class_prof_rel',
                                      column1='name',
                                      column2='f_name')
     subject_ids = fields.Many2many(comodel_name='university.subject',
                                      relation='class_sub_rel',
                                      column1='classroom_name',
                                      column2='name')