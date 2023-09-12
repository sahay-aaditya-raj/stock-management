from django import template
register = template.Library()


from num2words import num2words
import locale


def amount(value,amt):
    value = float(value)
    amt = float(amt)
    return value*amt

def num_words(value):
    
    return num2words(value, lang='en_IN').title()


def rond(value,places=0):
    value = float(value)
    if places == 0:
        return round(value)
    else:
        return round(value,places)

def num_comma(number):
    dec = '.'+str(number).split('.')[1] if len(str(number).split('.')) == 2 else ""
    locale.setlocale(locale.LC_NUMERIC, 'en_IN')  # Set the Indian locale
    formatted_number = locale.format_string("%d", number, grouping=True)
    return formatted_number+dec

def dictVal(dic,value):
    return dic[value]


def upr(value):
    return value.upper()

register.filter('amount',amount)
register.filter('num_words',num_words)
register.filter('round',rond)
register.filter('intcomma',num_comma)
register.filter('dictVal',dictVal)
register.filter('upper',upr)

@register.filter('multiply')
def multiply(value1,value2):
    return round(float(value1)*float(value2),2)

@register.filter('gstrate')
def gstrate(val1,val2):
    return round(float(val1) * float(val2) * 0.01,2)

@register.filter('total')
def total(val1,val2):
    return float(val1)*float(val2) * 0.02 + float(val1)