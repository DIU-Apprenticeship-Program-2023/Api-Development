# -- coding: utf-8 --
from odoo import http
# from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class AaaApiDevelop(http.Controller):
    @http.route('/aaa/api/develop/my_activity', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index(self, **kw):
        contact_list = http.request.env['crm.lead'].sudo().search([])
        return_contact_list = list()
        for contact in contact_list:

            http.request.env['model'].sudo().create(
                {
                 'name': contact.name,
                 'email_from': contact.email_from,
                 'phone': contact.phone,
                 'team_id': contact.team_id
                 }
            )

        return 'return_contact_list'

    @http.route('/aaa/api/develop/partner', auth='public', website=False, csrf=False, type='json', methods=['GET'])
    def index_2(self, **kw):
        contact_list = http.request.env['res.partner'].sudo().search([])
        return_contact_list = list()
        for contact in contact_list:
            # _logger.info(contact.name)
            return_contact_list.append({
                'Company Type': contact.company_type,
                'Phone Number': contact.phone,
                'Email Address': contact.email,
                'Address': contact.street
            })

        http.request.env['res.partner'].sudo().create(
            {
                'street': kw['street'],
                'name': kw['name'],
                'email': kw['email'],
                'phone': kw['phone']
            }
        )

        return kw
