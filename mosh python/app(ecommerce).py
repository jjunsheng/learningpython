# different ways to import
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
print("import")

from ecommerce import shipping
shipping.calc_tax()
shipping.calc_shipping()
print("from import")


from ecommerce.shipping import calc_shipping, calc_tax
calc_shipping()
calc_tax()
calc_shipping()
calc_tax()