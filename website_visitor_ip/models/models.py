import logging
import requests
from odoo import fields, models, api
from odoo.http import request
_logger = logging.getLogger(__name__)

class WebsiteVisitor(models.Model):
    _inherit = 'website.visitor'

    ip_address = fields.Char(string='IP Address', compute='_compute_ip_address', store=True)

    @api.depends()
    def _compute_ip_address(self):
        for visitor in self:
            visitor.ip_address = request.httprequest.environ['REMOTE_ADDR']

    # @staticmethod
    # def _get_visitor_ip():
      
    #    ip = request.httprequest.environ['REMOTE_ADDR']
    #    _logger.info("___________________>>>>>>>>IP<<<<<<<<____________________",ip)
    #    return ip
