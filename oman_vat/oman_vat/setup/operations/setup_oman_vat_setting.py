import frappe
import os
import json
from frappe.custom.doctype.custom_field.custom_field import create_custom_field

# adding to git

def create_oman_vat_setting(self, method):
    """
    On creation of first company. Creates OMAN VAT Setting"""
    # Validating if this is the first company for Saudi Arab
    company_list = frappe.get_all('Company', {
        'country': 'Oman'
    }) 

    oman_vat_setting = frappe.get_all('OMAN VAT Setting', {
        'company': self.name
    })

    if len(company_list) == 1 and len(oman_vat_setting) == 0:
        make_custom_fields()
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'oman_vat_settings.json')
        with open(file_path, 'r') as json_file:
            account_data = json.load(json_file)
        

        # Creating OMAN VAT Setting
        oman_vat_setting = frappe.get_doc({
            'doctype': 'OMAN VAT Setting',
            'company': self.name
        })
        
        for data in account_data:
            if data['type'] == 'Sales Account':
                for row in data['accounts']:
                    item_tax_template = row['item_tax_template']
                    account = row['account']
                    oman_vat_setting.append('oman_vat_sales_accounts', {
                        'title': row['title'],
                        'item_tax_template': f'{item_tax_template} - {self.abbr}',
                        'account': f'{account} - {self.abbr}'
                    })
                
            elif data['type'] == 'Purchase Account':
                for row in data['accounts']:
                    item_tax_template = row['item_tax_template']
                    account = row['account']
                    oman_vat_setting.append('oman_vat_purchase_accounts', {
                        'title': row['title'],
                        'item_tax_template': f'{item_tax_template} - {self.abbr}',
                        'account': f'{account} - {self.abbr}'
                    })

        oman_vat_setting.save()

def make_custom_fields():
    qr_code_field = dict(
        fieldname='qr_code', 
        label='QR Code', 
        fieldtype='Attach Image', 
        read_only=1, no_copy=1, hidden=1)
    customers_name_in_arabic = dict(
        fieldname='customers_name_in_arabic', 
        label='Customer Name in Arabic', 
        fieldtype='Read Only', 
        insert_after='customer_name',
        fetch_from='customer.customer_name_in_arabic', print_hide=1)
    
    create_custom_field('Sales Invoice', qr_code_field)
    create_custom_field('Sales Invoice',customers_name_in_arabic)
