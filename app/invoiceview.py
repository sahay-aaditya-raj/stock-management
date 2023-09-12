from .models import SavedInvoice, SaveEntries, SaveRateEntries

def View_Invoice(pk):
    sv_inv = SavedInvoice.objects.get(id=pk)
    sv_ents = SaveEntries.objects.filter(invoiceno = sv_inv.invoicenumber)
    sum_all = 0
    tot_qty = 0
    for sv_ent in sv_ents:
        sum_all += float(sv_ent.amount)
        tot_qty += sv_ent.qty + sv_ent.bonus
    gst = sv_inv.gst * 0.01
    gst = gst * sum_all
    total = gst + gst + sum_all
    
    if sv_ents[0].pts == '' or sv_ents[0].pts == None:
        evn = False
    else:
        evn = True
    return {'sv_inv':sv_inv,'sv_ents':sv_ents, 'sum_all':sum_all, 'gst':gst, 'total':total, 'tot_qty':tot_qty, 'pk':pk, 'evn':evn}


def View_Rate_Invoice(pk):
    sv_inv = SavedInvoice.objects.get(id=pk)
    sv_ents = SaveRateEntries.objects.filter(invoiceno = sv_inv.invoicenumber)
    sum_all = 0
    tot_qty = 0
    for sv_ent in sv_ents:
        sum_all += float(sv_ent.amount)
        tot_qty += sv_ent.qty
    gst = sv_inv.gst * 0.01
    gst = gst * sum_all
    total = gst + gst + sum_all
    
    return {'sv_inv':sv_inv,'sv_ents':sv_ents, 'sum_all':sum_all, 'gst':gst, 'total':total, 'tot_qty':tot_qty, 'pk':pk}