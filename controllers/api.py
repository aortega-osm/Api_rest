# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class PurchaseOrderController(http.Controller):

    @http.route('/api/purchase/insert', auth='user', methods=['POST'], csrf=False)
    def insert_purchase(self, **kw):
        try:
            data = json.loads(str(http.request.httprequest.data, 'utf-8'))
            new_purchase = http.request.env['purchase.order'].create({
                'user_id': data.get('user_id'),
                'partner_id': data.get('partner_id'),
                'company_id': data.get('company_id'),
                'currency_id': data.get('currency_id'),
                'picking_type_id': data.get('picking_type_id'),
                'order_line': [(0, 0, {
                    'product_id': line.get('product_id'),
                    'product_qty': line.get('product_qty'),
                    'price_unit': line.get('product_price'),
                })
                for line in data.get('lines', [])],
            })
            return json.dumps({'success': True, 'purchase_order_id': new_purchase.id})
        except Exception as e:
            return json.dumps({'err': str(e)})

    @http.route('/api/purchase_order/<int:order_id>', auth='public', methods=['GET'], csrf=False)
    def get_purchase_order(self, order_id):
        try:
            purchase_order = request.env['purchase.order'].sudo().browse(order_id)
            return json.dumps({
                'partner_id': purchase_order.partner_id.name,
                'user_id': purchase_order.user_id.name,
                'currency_id': purchase_order.currency_id.name,
                'company_id': purchase_order.company_id.name,
                'picking_type': purchase_order.picking_type_id.name,
                'amount_untaxed': purchase_order.amount_untaxed,
                'amount_tax': purchase_order.amount_tax,
                'amount_total': purchase_order.amount_total,
            })
        except Exception as e:
            return json.dumps({'error': str(e)})