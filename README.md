## OMAN VAT management and reporting - ERPNext module.

This is minor tweak of E-invoing done on ( https://github.com/ahmadpak/ksa_vat ) for Oman. Full credit goes to Havenir Solutions who has done most of the coding. 

VAT and E-invoicing are mostly same across the Gulf, because of implementaion of taxation is a GCC decision. However there are minor changes required, we at ERPGulf working with our partners and clients to accomodate such changes and publish it for the community to use.

We will soon publish VAT modules for other Gulf countries like Bahrain, Kuwait, and Qatar. ( VAT is not implemented in Qatar as of now ) . UAE and Saudi VAT modules are already available with ERPNext core.

Please send us your suggestions and feedback to support@erpgulf.com

Please visit our website www.ERPGulf.com  and our hosting provider www.Claudion.com  ( Claudion provides VMs, cloud servers, email and web hostings for Gulf  companies. hosted in Jeddah, Dubai and Doha. Provides fastest hosting service in your own city. ) 


How to install
--------------
bench get-app oman_vat https://github.com/ERPGulf/Oman_VAT.git

bench --site site1.local install-app oman_vat

bench --site site1.local migrate


If you face any issue with installation, send email to support@ERPGulf.com 

Functional documentation ( We have published a video documentation on Oman VAT on our youtube channel , please watch https://youtu.be/G3vo3oUaD2s ) 
-------------------------
Generate a report for the VAT on Sales and VAT on Purchases
![image](https://user-images.githubusercontent.com/69480716/153743642-9a3d61d0-cd4a-4951-8262-51f4210579bf.png)

Find the new Oman VAT report and Oman VAT settings document in the Accounting Workspace

Oman VAT Setting is mapping item Tax Template and Account to the respective title to be shown in the report

vat setting.png

Note: Multiple Item Tax Templates can be set for each item.

A good example in the sales would be an item that is treated as a standard rated Sales and as well as Zero-rated domestic sales. The same case can be applied to the purchase cycle.
![image](https://user-images.githubusercontent.com/69480716/153743664-f2e5eccd-820c-460b-822b-fc86d16cd71c.png)
Use the Item Tax Template in the Sales and Purchase Invoice. The data should result in a similar Oman VAT Report

![image](https://user-images.githubusercontent.com/69480716/153743675-83daeba8-4aa7-47fa-ae2f-46b1749f2bb2.png)

