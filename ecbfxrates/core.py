import requests
import xml.etree.ElementTree as ET
import pandas as pd


def get_ecb_rates(currency, start_period):
    # please see description of request structure here: https://sdw-wsrest.ecb.europa.eu/help/

    entrypoint = 'https://sdw-wsrest.ecb.europa.eu/service/'
    resource = 'data'  # The resource for data queries is always'data'
    flowRef = 'EXR'  # Dataflow describing the data that needs to be returned,
                    # exchange rates in this case
    key = 'D.' + currency + '.EUR.SP00.A'  # Defining the dimension values, D stands for daily,
    # followed by currency code, etc.
    parameters = {'startPeriod': start_period}

    request_url = entrypoint + resource + '/' + flowRef + '/' + key

    # Make the HTTP request
    response = requests.get(request_url, params = parameters)

    xml_data = response.text  # the data returned is in XML format, so we need to parse it
    root = ET.fromstring(xml_data)

    rate_list = []
    for k in range(2, len(root[1][0])):  # the data starts at xml-tree element root[1][0],
        # this can be checked by looking at recieved data in the browser
        date = root[1][0][k][0].attrib['value']
        rate = root[1][0][k][1].attrib['value']
        rate_list.append((date, rate))

    df = pd.DataFrame(rate_list)
    df.columns = ['date', 'rate_value']
    df['rate_value'] = pd.to_numeric(df['rate_value'], errors='coerce')
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(inplace=True)

    return df