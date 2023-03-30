import concurrent.futures, requests, re, base64, csv, io, openai, string, time
from pprint import pprint
from io import StringIO

output_buffer = io.StringIO()
headers = {
 'Host':'vfm4x0n23a-dsn.algolia.net',
 'Connection':'keep-alive',
 'Content-Length':'647',
 'sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
 'x-algolia-application-id':'VFM4X0N23A',
 'content-type':'application/x-www-form-urlencoded',
 'x-algolia-api-key':'Use Fiddler to get this value',
 'sec-ch-ua-mobile':'?0',
 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
 'sec-ch-ua-platform':'"macOS"',
 'Accept':'*/*',
 'Origin':'https://www.iheartjane.com',
 'Sec-Fetch-Site':'cross-site',
 'Sec-Fetch-Mode':'cors',
 'Sec-Fetch-Dest':'empty',
 'Referer':'https://www.iheartjane.com/',
 'Accept-Encoding':'gzip, deflate, br',
 'Accept-Language':'en-US,en;q=0.9'}


with open('flowers3', 'r') as f:
    thc_value = f.readline()


# Open the CSV file
with open('stores2', 'r') as file:
    for line in file:
        # process the line here
        number = int(line[:line.find(',')])
        info = line[line.find(','):]
        #print("Query store "+str(number))
        # Assign the digits to the variables in reverse order
        pos = number % 10
        pos2 = (number // 10) % 10
        pos3 = (number // 100) % 10
        pos4 = number // 1000
        payload = '{"requests":[{"indexName":"menu-products-by-price-eighth-ounce-production","params":"facets=%5B%5D&filters=root_types%3A\\\"flower\\\"%20AND%20available_weights%3A%22eighth%20ounce%22%20AND%20percent_thc%20%3E%3D%2025%20AND%20store_id%20%3D%201552%20AND%20kind%3A%22flower%22%20OR%20root_types%3A%22flower%22&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&highlightPreTag=%3Cais-highlight-0000000000%3E&hitsPerPage=48&optionalFilters=brand%3ARythm%3Cscore%3D5%3E%2Cbrand%3AGood%20Green%3Cscore%3D4%3E%2Cbrand%3ABetty%27s%20Eddies%2Cbrand%3Aincredibles%2Cbrand%3AMary%27s%20Medicinals%2Cbrand%3ADogwalkers%2Cbrand%3ARythm%20-%20Remix%2Cbrand%3ADr.%20Solomon%27s%2Cbrand%3A%26Shine&page=0&tagFilters=&userToken=WIx1kue3HisuiXeSos67v"}]}'
        # Insert the storeId variable into the payload
        storeId = number
        payload = payload.replace('1552', str(storeId))
        #print(payload)  # add this line
        payload = payload.replace('percent_thc%20%3E%3D%2025', 'percent_thc%20%3E%3D%20'+str(thc_value))
        response0 = requests.request("POST", "https://vfm4x0n23a-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.2)%3B%20Browser%3B%20JS%20Helper%20(3.11.1)%3B%20react%20(18.2.0)%3B%20react-instantsearch%20(6.36.0)", headers=headers, data=payload,verify=False)
        content = response0.json()

        #print(content)

        # Create a buffer to hold the output
        output_buffer = StringIO()

        # Call pprint() with the output_buffer as the argument
        pprint(content, stream=output_buffer)

        # Get the output from the buffer as a string
        output_string = output_buffer.getvalue()

        # Get the output from the buffer as a string
        content=output_string


        # Define the regular expressions for matching the relevant data
        regex1 = re.compile(r"'brand_subtype|'custom_product_subtype|-----|value': 'hybrid'|'value': 'sativa'|'value': 'indica'|brand'|bucket_price|'name'|'percent_thc'|=====|'available_weights'")
        regex2 = re.compile(r"params'|_highlightResult|matchLevel'")
        regex3 = re.compile(r"=====|:")
        regex4 = re.compile(r",|'|\\[|\\]|{|}")

        # Apply the regular expressions to extract the relevant data
        matches = []
        response=str(content)
        #pprint(response)
        #print("contentlength="+str(len(response)))
        try:
            for line in response.splitlines():
                 #print("splitting..")
                 if regex1.search(line) and not regex2.search(line):
                     #print("appended..")
                     matches.append(line)
                     data = ''.join(matches)
                     data = regex3.sub('', data)
                     data = regex4.sub('', data)
        except:
            print("didn't work.")

        # Write the extracted data to a file
        with open('ml_jane.txt', 'w') as f:
            f.write("StoreId: "+str(storeId)+", "+info)
            #print("StoreId: "+str(storeId)+", "+info)
            for match in matches:
                 f.write(str(match) + '\n')
                 #print(str(match))

        # Read and split the data into a list of dictionaries
        f.close()
        data = []
        header = []
        with open("ml_jane.txt", "r") as f:
            #    print("opened it for reading")
            for line in f:
                ##print("reading..")
                line = line.rstrip('\n')
                result = {}
                parts = line.split(":")
                for i in range(0, len(parts)-1, 2):
                    k = parts[i].strip()
                    v = parts[i+1].strip()
                    result[k] = v

                if len(parts) % 2 != 0:
                    result[parts[-1].strip()] = ""
                data.append(result)
        vbrand=vbrand_subtype=vcustom_product_subtype=vname=vthc=vthca=vprice=sendtochatgpt=""
        #print(len(data))
        for d in data:
            try:
                for key, value in d.items():
                    if 'value' in key and (value is not None) and ('None' not in value):
                        if 'indica' in value :
                            vtype = 'Indica'
                            #print("set vtype value "+value)
                        if 'sativa' in value :
                            vtype = 'Sativa'
                            #print("set vtype value "+value)
                        if 'hybrid' in value :
                            vtype = 'Hybrid'
                            #print("set vtype value "+value)
                    if ('brand' in key) and ((value is  None) or ('None' not in value)):
                        vbrand = value
                    if 'name' in key and (value is not None) and ('None' not in value):
                        vname = value+" "+vbrand_subtype+" "+vcustom_product_subtype     
                    if 'brand_subtype' in key and (value is not None) and ('None' not in value):
                        if "round" in value:
                            vbrand_subtype= "1"
                    if 'custom_product_subtype' in key and (value is not None) and ('None' not in value):
                        if "Shake" in value:
                            vbrand_subtype = "2"
                    if 'percent_thc'  in key : 
                        vthc = value
                        sendtochatgpt=sendtochatgpt+vbrand[:25]+","+vname[:50]+","+vtype[:10]+","+ vthc[:7]+","+ vthca[:7]+","+vprice[:5]+"\n"
                    if 'percent_thca' in key and (value is not None) and ('None' not in value):
                        vthca = max(value,vthc,thca)
                    if 'bucket_price' in key and (value is not None) and ('None' not in value):
                        vprice = "$"+str(value)
            except:
                continue     
        # Set OpenAI API key
        openai.api_key = "put your openai api key here"
        # Function to process OpenAI request
        def process_request(name):
            try:
                response = openai.Completion.create(
                    prompt =  "We are reviewing a list of cannabis strains. write a 6 line review of the online cannabis menu. if you are aware of the traits of the strain please include them briefly.  Review this next sorted list, if possible for each strain types recommend only the best value  Hybrid, Indica, and Sativa strains by only the price in $  which is always the last field. The quantity is always 3.5 grams. You msust  calculate the cost per gram. talk about the brand, name, THC, and price for each strain and cost per gram  while counting the number of items.  At the beginning list the storeId and Name and Address.  At the end, mention the number of items in the list. The store number is "+str(storeId)+" and the address is  "+info+s,

                    #prompt = "write an analytical 6 line summary of the online cannabis menu. if you are aware of the traits of the strain please include them briefly.  Review this next sorted list, if possible for each strain types recommend only the best value  Hybrid, Indica, and Sativa strains by only the price in $  which is always the last field. The quantity is always 3.5 grams. You msust  calculate the cost per gram. talk about the brand, name, THC, and price for each strain and cost per gram  while counting the number of items.  At the beginning list the storeId and Name and Address.  At the end, mention the number of items in the list. The store number is "+str(storeId)+" and the address is  "+info+s,
                    model="text-davinci-003",
                    temperature=0,
                    max_tokens=2000,
                    top_p=1,
                    frequency_penalty=0,
                    timeout=15,
                    presence_penalty=1
                )
                return response.choices[0].text
            except:
                return None
        # Use a thread pool executor to process requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            if 1==1 :
                try:
                    # Get user input and clean it
                    #s = input("Please enter your argument: ")
                    s = sendtochatgpt
                    #print("Sending: "+s)
                    #s = s.translate(str.maketrans("", "", string.punctuation + "'"))
                    # Start timer and submit request
                    start_time = time.time()
                    future = executor.submit(process_request, s)
                    response = future.result(timeout=15)
                    # End timer and check response time
                    end_time = time.time()
                    if end_time - start_time > 15:
                        print("Sorry, the response took too long.")
                    # Print response
                    print(response)
                    # Exit loop if user input is "quit"
                except KeyboardInterrupt:
                    print("\nKeyboardInterrupt received. Exiting.")
                except Exception as e:
                    print("The request timed out.", str(e))


