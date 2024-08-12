# -*- coding: utf-8 -*-
# from odoo import http


# class rokilibrary(http.Controller):
#     @http.route('/rokilibrary/rokilibrary', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rokilibrary/rokilibrary/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('rokilibrary.listing', {
#             'root': '/rokilibrary/rokilibrary',
#             'objects': http.request.env['rokilibrary.rokilibrary'].search([]),
#         })

#     @http.route('/rokilibrary/rokilibrary/objects/<model("rokilibrary.rokilibrary"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rokilibrary.object', {
#             'object': obj
#         })
