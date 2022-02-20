from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in oman_vat/__init__.py
from oman_vat import __version__ as version

setup(
	name='oman_vat',
	version=version,
	description='OMAN VAT Management and Reporting',
	author='ERPGulf.com',
	author_email='support@erpgulf.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
