import os
num_data = int(os.environ.get('NUM_DATA', 1000))
xml_str = '<?xml version="1.0" encoding="UTF-8"?><array xmlns="http://www.w3.org/2005/xpath-functions">'
for i in range(1, num_data+1):
    xml_str += f'<map><number key="id">{i}</number><string key="name">Product {i}</string><number key="price">{i*10}</number><array key="tags"><string>tag1</string><string>tag2</string></array><map key="dimensions"><number key="length">{i*2}</number><number key="width">{i*3}</number><number key="height">{i*4}</number></map><map key="warehouseLocation"><number key="latitude">{i*5}</number><number key="longitude">{i*6}</number></map></map>'

xml_str += '</array>'
print(xml_str)
