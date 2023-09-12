from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

from .models import *
import json
import datetime

from .invoiceview import View_Invoice, View_Rate_Invoice
# Create your views here.


def tempMsg(request,msg):
    context={'message':msg}
    return render(request, 'msg.html', context)


def home(request):
    context = {}
    return render(request, 'home.html', context )



#invoice list
def invoice_list(request):
    savedInvoices = SavedInvoice.objects.all()
    savedInvoices = savedInvoices.order_by('-invoicenumber')
    sv_inv_list = list()
    for savedInvoice in savedInvoices:
        amount = 0
        if not savedInvoice.rate:
            savedEntries = SaveEntries.objects.filter(invoiceno=savedInvoice.invoicenumber)
            for savedEntry in savedEntries:
                amount += float(savedEntry.amount)
        
        elif savedInvoice.rate:
            savedEntries = SaveRateEntries.objects.filter(invoiceno=savedInvoice.invoicenumber)
            for savedEntry in savedEntries:
                amount += float(savedEntry.amount)
            
        amount = round(amount + amount*savedInvoice.gst*0.01*2, 2)
        
        dic = {'inv': savedInvoice.invoicenumber,
               'name': savedInvoice.name.upper(),
               'date': str(savedInvoice.date.strftime("%d-%B-%Y")),
               'gstid': savedInvoice.gstid,
               'dlno': savedInvoice.dlno.upper(),
               'city': savedInvoice.city.upper(),
               'paid': savedInvoice.paid,
               'amount': amount,
               'id': str(savedInvoice.id),
               }
        sv_inv_list.append(dic)
        
    paid_invoices = SavedInvoice.objects.filter(paid=True)
    unpaid_invoices = SavedInvoice.objects.filter(paid=False)
    
    paid_amt,unpaid_amt = 0,0
    
    try:
        for paid_invoice in paid_invoices:
            if paid_invoice.rate:
                paid_ents = SaveRateEntries.objects.filter(invoiceno = paid_invoice.invoicenumber)
            
            elif not paid_invoice.rate:
                paid_ents = SaveEntries.objects.filter(invoiceno = paid_invoice.invoicenumber)
                
            amt = 0
            for paid_ent in paid_ents:
                amt = amt + float(paid_ent.amount)
                
            paid_amt += amt + amt*paid_invoice.gst*0.01*2
        paid_amt = round(paid_amt)
        
    except:
        paid_amt = 0
        
    try:
        for unpaid_invoice in unpaid_invoices:
            if not unpaid_invoice.rate:
                unpaid_ents = SaveEntries.objects.filter(invoiceno = unpaid_invoice.invoicenumber)
                
            elif unpaid_invoice.rate:
                unpaid_ents = SaveRateEntries.objects.filter(invoiceno = unpaid_invoice.invoicenumber)
                
            amt = 0
            for unpaid_ent in unpaid_ents:
                amt = amt + float(unpaid_ent.amount)
                
            unpaid_amt += amt + amt*unpaid_invoice.gst*0.01*2
            
        
        unpaid_amt = round(unpaid_amt)
        
    except:
        unpaid_amt = 0
    
    context = {'sv_inv_list': json.dumps(sv_inv_list),'paid':paid_amt, 'unpaid':unpaid_amt}
    return render(request, 'invoice_list.html', context )





def stocks(request):
    all_stocks = Stock.objects.all()
    stock_json = []
    products = Products.objects.all()
    
    for all_stock in all_stocks:
       var = {'id':all_stock.id,'name':all_stock.product.name.upper(), 'batch':all_stock.batch.upper(),'manufacturer':all_stock.product.manufacturer.name.upper(),'pack':all_stock.product.volume,'expiry':str(all_stock.expiry.strftime('%m-%Y')),'quantity':all_stock.quantity} 
       stock_json.append(var)
    
    err = False
    if request.method == 'POST':
        try:
            product = Products.objects.get(id=request.POST.get('product'))
            batch = request.POST.get('batch')
            quantity = int(request.POST.get('quantity'))
            date = request.POST.get('date')
            stock = Stock.objects.create(product=product,batch=batch,quantity=quantity,expiry=date)
            stock.save()
            return redirect('stocks')
        except Exception as e:
            err = True
    
    context = {'json_stock':json.dumps(stock_json), 'products':products,'err':err}
    return render(request, 'stocks.html', context )



def stockDel(request, pk):
    stock = Stock.objects.get(id=pk)
    stock.delete()
    return redirect('stocks')


def productList(request):
    products = Products.objects.all()
    manufacturers = Manufacturers.objects.all()
    json_product = []
    for product in products:
        var = {'name':product.name.upper(), 'manufacturer':product.manufacturer.name.upper(), 'pack':product.volume}
        json_product.append(var)
        
    err = False
    if request.method == 'POST':
        try:
            manufacturer = Manufacturers.objects.get(id=request.POST.get('manufacturer'))
            name = request.POST.get('name')
            pack = request.POST.get('pack')
            nw_pro = Products.objects.create(manufacturer=manufacturer, name=name, volume=pack)
            nw_pro.save()
            return redirect('products')
        except Exception as e:
            err = True
            
        
    context={'json_stock':json.dumps(json_product), 'manufacturers':manufacturers, 'err':err}
    
    return render(request, 'product.html', context)


def manufacturer(request):
    manufacturers = Manufacturers.objects.all()
    
    json_list = []
    for manufacturer in manufacturers:
        var = {'name':manufacturer.name, 'address':manufacturer.address, 'alias':manufacturer.alias}
        json_list.append(var)
        
    err = False    
    if request.method == 'POST':
        try:
            name = request.POST.get('manufacturer')
            address = request.POST.get('address')
            alias = request.POST.get('alias')
            nwmfg = Manufacturers.objects.create(name=name,address= address, alias=alias)
            nwmfg.save()
            return redirect('manufacturer')
        except Exception as e:
            err = False
    
    context = {'json_stock':json.dumps(json_list), 'err':err}
    return render(request, 'manufactreres.html', context)


def party(request):
    parties = Party.objects.all()
    json_party = []
    for party in parties:
        var = {'id':party.id, 'name':party.name, 'add1':party.addressLine_1,'add2':party.addressLine_2, 'add3':party.addressLine_3, 'gstid':party.gstid, 'dlno':party.dlno,'city':party.city}
        json_party.append(var)
        
    context = {'party':json.dumps(json_party)}
    return render(request, 'party.html', context)


def partyView(request, pk):
    err,msg = False,None
    party = Party.objects.get(id=pk)
    party_info = {'name':party.name, 'dlno':party.dlno, 'gst':party.gstid, 'city':party.city,
                  'add1':party.addressLine_1, 'add2':party.addressLine_2, 'add3':party.addressLine_3,"mbno":party.mbno}
    
    if request.method == 'POST':
        try:
            party.name = request.POST.get('name')
            party.dlno = request.POST.get('dlno')
            party.gstid = request.POST.get('gst')
            party.city = request.POST.get('city')
            party.addressLine_1 = request.POST.get('add1')
            party.addressLine_2 = request.POST.get('add2')
            party.addressLine_3 = request.POST.get('add3')
            party.mbno = request.POST.get('mbno')
            party.save()
            return redirect('party')
        except Exception as e:
            err = True
            msg = 'Something Went Wrong'
                
    context = {'party':json.dumps(party_info),'err':err,'msg':msg}
    return render(request, 'view_party.html', context)


def addParty(request):
    err,msg = False,None
    if request.method == 'POST':
        try:
            if request.POST.get('name')!='' and request.POST.get('gst')!='' and request.POST.get('dlno')!='' and request.POST.get('add1')!='' and request.POST.get('city')!='' and request.POST.get('mbno') !='' :
                party = Party.objects.create(
                    name = request.POST.get('name'),
                    addressLine_1 = request.POST.get('add1'),
                    gstid = request.POST.get('gst'),
                    dlno = request.POST.get('dlno'),
                    city = request.POST.get('city'),
                    addressLine_2 = request.POST.get('add2'),
                    addressLine_3 = request.POST.get('add3'),
                    mbno = request.POST.get('mbno')
                )
                party.save()
                return redirect('party')
            else:
                err=True
                msg = '* fields are COMPULSORY !'
                
        except Exception as e:
            err=True
            msg='Try Again !'
            
            
    context ={'err':err,'msg':msg}
    return render(request, 'new_party.html', context)




def new_invoice_menu(request):
    invoices = SavedInvoice.objects.all()
    parties = Party.objects.all()
    inv_count = []
    
    for invoice in invoices:
        inv_count.append(invoice.invoicenumber)
        
        
    if request.method == 'POST':
        try:
            costumer  = Party.objects.get(id=request.POST.get("party"))
            if request.POST.get("date") == '':
                date = datetime.date.today()
            else:
                date = request.POST.get("date")
                
            inv = Invoice.objects.create(
                invoicenumber = request.POST.get("invoice"),
                costumer = costumer,
                gstrate = 9 if request.POST.get("gstrate") == 'nine' else 6,
                typeofinv = True if request.POST.get("invType")=='rate' else False,
                date = date
            )
            inv.save()
            return redirect('new-temp-inv',pk=inv.id)
        except Exception as e:
            raise e
        
        
    context = {'inv_list':inv_count, 'parties':parties}
    return render(request,'new-inv-menu.html', context)


def new_temp_inv(request,pk):
    inv = Invoice.objects.get(id=pk)
    products = Products.objects.all()
    stocks = Stock.objects.all()
    
    
    if inv.typeofinv:
        ents = RateEntry.objects.filter(inv=inv)
        amt = 0
        ent = {}
        qty = 0
        for i in range(ents.count()):
            ent[f'{i+1}'] = ents[i]
            amt += ents[i].rate * ents[i].qty
            qty += ents[i].qty
            
                
        json_stock = []
        for stock in stocks:
            var = {'id':stock.id, 'name':stock.product.name, 'batch':stock.batch, 'expiry': str(stock.expiry.strftime('%m/%Y')),'quantity':stock.quantity}
            json_stock.append(var)
            
        if request.method == 'POST':
            product = Stock.objects.get(id=int(request.POST.get('stock')))
            mrp = float(request.POST.get('mrp'))
            rate = float(request.POST.get('rate'))
            quantity = int(request.POST.get('qty'))
            
            nw_rate_ent = RateEntry.objects.create(
                inv = inv,
                product = product,
                mrp = mrp,
                rate = rate,
                qty = quantity
            )
            nw_rate_ent.save()
            return redirect('new-temp-inv',pk=inv.id)
            
        context = {'inv':inv,'ent':ent, 'products':products,'json_stock':json.dumps(json_stock), 'amt':amt, 'qty':qty}
        return render(request, 'new_rate_inv.html', context)    
            
    
    elif not inv.typeofinv:
        ents = Entry.objects.filter(inv=inv)
        amt = 0
        ent = {}
        qty = 0
        for i in range(ents.count()):
            ent[f'{i+1}'] = ents[i]
            qty += ents[i].qty + ents[i].bonus
            if ents[i].pts != None:
                amt += ents[i].pts * ents[i].qty
            else :
                amt += ents[i].ptr * ents[i].qty
        
        json_stock = []
        for stock in stocks:
            var = {'id':stock.id, 'name':stock.product.name, 'batch':stock.batch, 'expiry': str(stock.expiry.strftime('%m/%Y')),'quantity':stock.quantity}
            json_stock.append(var)
            
        if request.method == 'POST':
            product = Stock.objects.get(id=int(request.POST.get('stock')))
            mrp = float(request.POST.get('mrp'))
            ptr = float(request.POST.get('ptr'))
            bonus = float(request.POST.get('bonus'))
            qty = float(request.POST.get('qty'))
            
            if request.POST.get('pts') != '':
                pts = float(request.POST.get('pts'))
            else:
                pts=None
            
            ne_ent = Entry.objects.create(
                inv=inv,
                product=product,
                mrp=mrp,
                ptr=ptr,
                pts=pts,
                qty=qty,
                bonus=bonus
            )
            ne_ent.save()
            return redirect('new-temp-inv',pk=inv.id)
            
        context = {'inv':inv,'ent':ent, 'products':products,'json_stock':json.dumps(json_stock), 'amt':amt, 'qty':qty}
        return render(request, 'new_inv.html', context)
    
    else:
        return redirect('home')
    
    
def del_ent(request,pk):
    ent = Entry.objects.get(id=pk)
    inv = ent.inv.id
    ent.delete()
    return redirect('new-temp-inv',pk=inv)


def del_rateEnt(request,pk):
    ent = RateEntry.objects.get(id=pk)
    inv = ent.inv.id
    ent.delete()
    return redirect('new-temp-inv', pk=inv)    


def saveinvoice(request,pk):
    inv = Invoice.objects.get(id=pk)
    ents = Entry.objects.filter(inv=inv)
    
    sv_inv = SavedInvoice.objects.create(
        invoicenumber = inv.invoicenumber,
        name=inv.costumer.name,
        address1=inv.costumer.addressLine_1,
        address2=inv.costumer.addressLine_2,
        address3=inv.costumer.addressLine_3,
        mbno=inv.costumer.mbno,
        city=inv.costumer.city,
        date=inv.date,
        gstid=inv.costumer.gstid,
        dlno=inv.costumer.dlno,
        gst=inv.gstrate,
        paid=False,
        rate=False,
    )
    
    a=1
    for ent in ents:
        sv_ent = SaveEntries.objects.create(
            invoiceno=ent.inv.invoicenumber,
            sno=a,
            description=ent.product.product.name.upper(),
            pack=ent.product.product.volume,
            mfg=ent.product.product.manufacturer.alias.upper(),
            batchNo=ent.product.batch.upper(),
            expiry=ent.product.expiry.strftime('%m/%Y'),
            mrp=ent.mrp,
            ptr=ent.ptr,
            pts= None if ent.pts == None else ent.pts,
            qty=ent.qty,
            bonus=ent.bonus,
            amount= ent.ptr*ent.qty if ent.pts==None else ent.pts*ent.qty
        )
        a+=1
        stock = Stock.objects.get(id=ent.product.id)
        stock.quantity = stock.quantity - (int(ent.bonus)+int(ent.qty))
        stock.save()
        sv_ent.save()
        ent.delete()
        
    sv_inv.save()
    
    return redirect('invoice-list')


def viewSavedInvoice(request,pk):
    svin = SavedInvoice.objects.get(id=pk)
    
    if not svin.rate:
        context = View_Invoice(pk)
        if request.method == 'GET':
            q = request.GET.get('q')
            if q=='ok':
                svin.paid=True
                svin.save()
                return redirect('view-saved-invoice', pk=pk)
            elif q=='no':
                svin.paid=False
                svin.save()
                return redirect('view-saved-invoice', pk=pk)
                
        return render(request,'view-invoice.html',context)
    
    if svin.rate:
        context = View_Rate_Invoice(pk)
        if request.method == 'GET':
            q = request.GET.get('q')
            if q=='ok':
                svin.paid=True
                svin.save()
                return redirect('view-saved-invoice', pk=pk)
            elif q=='no':
                svin.paid=False
                svin.save()
                return redirect('view-saved-invoice', pk=pk)
                
        return render(request,'view-invoice.html',context)


def pdfview(request,pk):
    svin = SavedInvoice.objects.get(id=pk)
    
    if not svin.rate:
        context = View_Invoice(pk)
        
    elif svin.rate:
        context = View_Rate_Invoice(pk)
        
    context['company'] = CompanyDetails.objects.all()[0]
    return render(request,'pdfview.html',context)


def saveRateInv(request,pk):
    inv = Invoice.objects.get(id=pk)
    ents = RateEntry.objects.filter(inv=inv)
    
    sv_inv = SavedInvoice.objects.create(
        invoicenumber = inv.invoicenumber,
        name=inv.costumer.name,
        address1=inv.costumer.addressLine_1,
        address2=inv.costumer.addressLine_2,
        address3=inv.costumer.addressLine_3,
        mbno=inv.costumer.mbno,
        city=inv.costumer.city,
        date=inv.date,
        gstid=inv.costumer.gstid,
        dlno=inv.costumer.dlno,
        gst=inv.gstrate,
        paid=False,
        rate = True
    )
    
    a=1
    for ent in ents:
        sv_ent = SaveRateEntries.objects.create(
            invoiceno=ent.inv.invoicenumber,
            sno=a,
            description=ent.product.product.name.upper(),
            pack=ent.product.product.volume,
            mfg=ent.product.product.manufacturer.alias.upper(),
            batchNo=ent.product.batch.upper(),
            expiry=ent.product.expiry.strftime('%m/%Y'),
            mrp=ent.mrp,
            rate=ent.rate,
            qty=ent.qty,
            amount= ent.rate*ent.qty
        )
        a+=1
        stock = Stock.objects.get(id=ent.product.id)
        stock.quantity = stock.quantity - int(ent.qty)
        stock.save()
        sv_ent.save()
        ent.delete()
        
    sv_inv.save()
    
    return redirect('invoice-list')