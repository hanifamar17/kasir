from django import template

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        value = float(value)
        # Format Rupiah dengan titik ribuan dan koma desimal
        return f"Rp {value:,.2f}".replace(',', '.').replace('.', ',', 1)
    except (ValueError, TypeError):
        return value
