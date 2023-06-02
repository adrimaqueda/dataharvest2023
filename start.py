import http.client

conn = http.client.HTTPSConnection("services.chanel.com")

payload = "division%5B%5D=1&division%5B%5D=2&division%5B%5D=5&division%5B%5D=3&productline%5B%5D=1&productline%5B%5D=2&productline%5B%5D=3&productline%5B%5D=4&productline%5B%5D=26&productline%5B%5D=5&productline%5B%5D=18&productline%5B%5D=19&productline%5B%5D=25&productline%5B%5D=10&productline%5B%5D=14&productline%5B%5D=13&productline%5B%5D=12&chanel-only=1&geocodeResults=%5B%7B%22address_components%22%3A%5B%7B%22long_name%22%3A%22Mosc%C3%BA%22%2C%22short_name%22%3A%22Mosc%C3%BA%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Moscow%22%2C%22short_name%22%3A%22Moscow%22%2C%22types%22%3A%5B%22administrative_area_level_2%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Mosc%C3%BA%22%2C%22short_name%22%3A%22Mosc%C3%BA%22%2C%22types%22%3A%5B%22administrative_area_level_1%22%2C%22political%22%5D%7D%2C%7B%22long_name%22%3A%22Rusia%22%2C%22short_name%22%3A%22RU%22%2C%22types%22%3A%5B%22country%22%2C%22political%22%5D%7D%5D%2C%22formatted_address%22%3A%22Mosc%C3%BA%2C%20Rusia%22%2C%22geometry%22%3A%7B%22bounds%22%3A%7B%22south%22%3A55.142591%2C%22west%22%3A36.8032249%2C%22north%22%3A56.0214609%2C%22east%22%3A37.9678221%7D%2C%22location%22%3A%7B%22lat%22%3A55.755826%2C%22lng%22%3A37.6173%7D%2C%22location_type%22%3A%22APPROXIMATE%22%2C%22viewport%22%3A%7B%22south%22%3A55.142591%2C%22west%22%3A36.8032249%2C%22north%22%3A56.0214609%2C%22east%22%3A37.9678221%7D%7D%2C%22place_id%22%3A%22ChIJybDUc_xKtUYRTM9XV8zWRD0%22%2C%22types%22%3A%5B%22locality%22%2C%22political%22%5D%7D%5D&radius=32.58181818181818"

headers = {
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'x-requested-with': "XMLHttpRequest"
    }

conn.request("POST", "/es_ES/storelocator/getStoreList", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
