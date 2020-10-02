# -*- coding: utf-8 -*-
# from odoo import http


# class EarlyBird(http.Controller):
#     @http.route('/early_bird/early_bird/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/early_bird/early_bird/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('early_bird.listing', {
#             'root': '/early_bird/early_bird',
#             'objects': http.request.env['early_bird.early_bird'].search([]),
#         })

#     @http.route('/early_bird/early_bird/objects/<model("early_bird.early_bird"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('early_bird.object', {
#             'object': obj
#         })
