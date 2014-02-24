from openerp.osv import osv, fields
import netsvc
import decimal_precision as dp
# import openerp.addons.decimal_precision as dp
import time
from tools.translate import _

class product_product(osv.osv):
    _name="product.product"
    _inherit='product.product'
    
 
    
    def create(self, cr, uid, vals, context=None):
        obj_id = super(product_product, self).create(cr, uid, vals, context=context)
        for val in self.browse(cr,uid,[obj_id]):
            #print 'finding match for product default code ' + str(val.default_code)
            product_id=self.search(cr,uid,[('default_code','=',val.default_code),('id','!=',val.id)])
            if len(product_id)>0:
                #print 'duplicate found'
                raise osv.except_osv(('Warning'),("Please choose different code"))        
        return obj_id
    
    
    def write(self, cr, uid, ids,vals, context=None):
        obj_id = super(product_product, self).write(cr, uid,ids, vals, context=context)
        for val in self.browse(cr,uid,ids):
            #print 'finding match for product default code ' + str(val.default_code)
            product_id=self.search(cr,uid,[('default_code','=',val.default_code),('id','!=',val.id)])
            if len(product_id)>0:
                #print 'duplicate found'
                raise osv.except_osv(('Warning'),("Please choose different code"))        
        return obj_id