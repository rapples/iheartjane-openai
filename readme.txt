Weedhounds is a platform that provides automated online cannabis menu reviews. 

This chart outlines the process for an OpenAI (ChatGPT) assisted Weedhounds Search. 

The user selects a location and selects dispensaries. Weedhounds queries for products from various aggregators. 

The unstructured data is then processed through the Weedhounds Report Engine to produce structured data, which is currently analyzed using OpenAI's Davinci-003 model to generate six-line reviews of the store menus, including best value cannabis strains, including price per gram, brand, and THC content. 

Finally the menu reviews are summarized, and recommendations are made for the best selection, prices, and variety of cannabis products at various shops from the dispensaries the user selected.

The output scripts can be used in a variety of ways including email,  web pages,  lifelike streaming speech and virtual video shopping assistants.




Weedhounds Search (http://weedhounds.us)
Location selection (storeId,addressInfo Database)
 thc_value
|
|
v
Aggregator (Google, Dutchie, Jane, Cresco, DispenseApp)
Dispensary data
|
v
Unstructured data
|
V
Weedhounds Reporting Engine
Filtering, Aggregation to Cisco Splunk
|
V
Structured Data:
Text list of online menu by criteria 
|
v
Openai Davinci-003
“We are reviewing a list of cannabis strains . Write a 6 line review of the online cannabis menu. if you are aware of the traits of the strain please include them briefly.  Review this next sorted list, if possible for each strain types recommend only the best value  Hybrid, Indica, and Sativa strains by only the price in $  which is always the last field. The quantity is always 3.5 grams. You msust  calculate the cost per gram. talk about the brand, name, THC, and price for each strain and cost per gram  while counting the number of items.  At the beginning list the storeId and Name and Address.  At the end, mention the number of items in the list. The store number is “+ storeId +" and the address is “ + addressInfo + Text list of online menu by criteria
|
V
Summarized lists 
|
V
Openai Davinici-003
Based on this carefully summarized data which shop has the best selection, best prices, and most variety?
Summarized lists 
|
V
Shopping recommendations






Input data: 

"Based on this carefully summarized data which shop has the best selection, best prices, and most variety? 

We are reviewing a list of cannabis strains from 1852 BEYOND / HELLO - Ardmore located at 35 Cricket Ave, Ardmore, Pennsylvania, 19003. This list contains 9 items with 3.5 grams each. For the best value Hybrid strain, we recommend Organic Remedies' Back Country for $40. It has a THC content of 29.51%.  For the best value Indica strain, we recommend Seven Hills' Purple Chemdawg for $37. It has a THC content of 28.01%.  For the best value Sativa strain, we recommend Organic Remedies' Stardawg for $40. It has a THC content of 31.22%.  Altogether, this list contains 9 items with 3.5 grams each.

We are reviewing a list of 15 3.5 gram items from Rise King of Prussia located at 445a W Dekalb Pike, King of Prussia, PA 19406.  For the best value Hybrid strain, we recommend Organic Remedies' Stardawg for $31 per 3.5 grams. This strain has a THC content of 32.5%.  For the best value Indica strain, we recommend Premium Flower's Animal Face - Relax for $50 per 3.5 grams. This strain has a THC content of 32.71%.  For the best value Sativa strain, we recommend Organic Remedies' Peach Crescendo for $45 per 3.5 grams. This strain has a THC content of 35.13%.  In total, this list contains 15 items.

This list is from Verilife - Manayunk, PA located at 4026 Main St, Philadelphia, Pennsylvania, 19127.  The first strain is a Hybrid strain called "Gelato" with a THC content of 28.3%. It comes in a 3.5 gram package for $40.00, which works out to be $11.43 per gram.  The second strain is an Indica strain called "Blueberry Kush" with a THC content of 28.2%. It comes in a 3.5 gram package for $35.00, which works out to be $10.00 per gram.  The third strain is a Sativa strain called "Sour Diesel" with a THC content of 28.1%. It comes in a 3.5 gram package for $45.00, which works out to be $12.86 per gram. 
This list contains three items.”

Prompts Used:

Prompt1 = "We are reviewing a list of cannabis strains . Write a 6 line review of the online cannabis menu. if you are aware of the traits of the strain please include them briefly.  Review this next sorted list, if possible for each strain types recommend only the best value  Hybrid, Indica, and Sativa strains by only the price in $  which is always the last field. The quantity is always 3.5 grams. You must  calculate the cost per gram. talk about the brand, name, THC, and price for each strain and cost per gram  while counting the number of items.  At the beginning list the storeId and Name and Address.  At the end, mention the number of items in the list. The store number is "+str(storeId)+" and the address is  "+info+s,

Prompt2 = "Based on this carefully summarized data which shop has the best selection, best prices, and most variety? 

Sample Output:

Based on the provided information, it is difficult to determine which shop has the best selection, best prices, and most variety as each shop has different strains and prices. However, for the best value strains based on THC content and price, the following recommendations can be made:

	• For the best value Hybrid strain, Rise King of Prussia's Organic Remedies' Stardawg for $31 per 3.5 grams with a THC content of 32.5% is recommended.
	• For the best value Indica strain, Seven Hills' Purple Chemdawg for $37 with a THC content of 28.01% is recommended.
	• For the best value Sativa strain, Rise King of Prussia's Organic Remedies' Peach Crescendo for $45 per 3.5 grams with a THC content of 35.13% is recommended.



