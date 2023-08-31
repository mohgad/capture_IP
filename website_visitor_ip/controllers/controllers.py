# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteVisitor(http.Controller):
#     @http.route('/website_visitor/website_visitor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_visitor/website_visitor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_visitor.listing', {
#             'root': '/website_visitor/website_visitor',
#             'objects': http.request.env['website_visitor.website_visitor'].search([]),
#         })

#     @http.route('/website_visitor/website_visitor/objects/<model("website_visitor.website_visitor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_visitor.object', {
#             'object': obj
#         })
