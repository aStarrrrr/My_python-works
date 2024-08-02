# import pdfkit
# pdfkit.from_file('test.html', 'out.pdf')

import pdfkit

# Specify the path to wkhtmltopdf executable
config = pdfkit.configuration(wkhtmltopdf='C:/path/to/wkhtmltopdf')

# Use the configuration in pdfkit.from_url
pdfkit.from_url('https://www.google.co.in/', 'shaurya.pdf', configuration=config)
