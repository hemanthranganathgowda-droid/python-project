from barcode_decoder import barcode_decoder
barcode_string="Mango_merchants@572122"

result = barcode_decoder.decode(barcode_string)
print(result)