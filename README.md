# Challenge-GIANT

Following to the documentation, was possible implemented a soluction for the problem descript. Where the challenge is to identify the most profitable period from the beginning of 2000 to beginning of March/2021.

We will now follow the code step by step to solve the problem:


Imports:

![image](https://github.com/user-attachments/assets/4ca2a877-5f53-47d3-9262-3235bbaedff0)

 
The main thing is to import pandas and requests:

 
 --  Pandas library for data conversion and formatting. In addition to reading, filtering, calculating and generating structured outputs.
 
 --  Requests is used to fetch data from an online API, specifically the Central Bank of Brazil API, which provides Selic rate data.


 “CarregadorSelic” Class:

 ![image](https://github.com/user-attachments/assets/8af3f600-b6c3-4e40-ba45-88306795f1ca)


 --  The “CarregadorSelic” Class, causes the API URL to be automatically set to specified date range.


 ![image](https://github.com/user-attachments/assets/357e79a4-bc7f-4aec-9afe-5d95f9640936)

 -- 	Defines the __init__ constructor method that will be called when a new instance of the class is created.
 --  Accepts two optional parameters, start_date and end_date, with default values of ‘01/01/2000’ and ‘03/01/2021’.


 ![image](https://github.com/user-attachments/assets/219c98c2-86e6-46b6-80e9-22b35fd8cc5e)

 --  These three code snippets initialize the “start_date and end_date” attributes and configure the Selic API URL based on the dates provided.


 <br/><br/>

 “Buscar_dados_selic” Method:

 ![image](https://github.com/user-attachments/assets/2543a064-150b-4ca2-b660-87cc19afaf3a)


 --  The “Buscar_dados_selic” method makes an HTTP GET requests to the API URL stored in self.url_selic. If the requests is successful (status code 200), it returns the data in JSON format. Otherwise, it raises an exception.

 
<br/>

“Processar_dados_selic” Method:

![image](https://github.com/user-attachments/assets/1aa8a719-9087-48db-9c7c-2fffa0b6d33c)

--  The “Processar_dados_selic” Method transforms Selic API data into a Pandas DataFrame, with the date column converted to date format and the value column converted to float and adjusted to by scale (divided by 100).



<br/>

“Obter_dataframe_selic” Method:

![image](https://github.com/user-attachments/assets/f26824db-0314-42e3-a61a-cf04d9d023ca)

--  The “Obter_dataframe_selic” method encapsulates the logic of fetching, searching and returning Selic data in an organized and efficient way.


<br/>

“Calcular_valor_ganho” Method:

![image](https://github.com/user-attachments/assets/cbaa7195-c684-4b4c-b9be-527212759440)

--  The “Calcular_valor_ganho” method is designed to calculate the value gained from invested capital over a specific period, using daily Selic rates.


<br/>

“Calcular_melhor_perido” Method:

![image](https://github.com/user-attachments/assets/68d48741-43e6-4ad6-aba4-91b701d1b023)


--  Using “calcular_melhor_periodo”. It is possible to identify which maximizes capital gains based on the Selic rate.

![image](https://github.com/user-attachments/assets/0b4ae639-c548-4de0-a534-fd5e2328d972)

--  If the gain calculated for the current period (gain_value) is greater than best_value, the method updates best_start, best_end and best_value with the values corresponding to the current period.
--  After going through all possible periods, the method returns the start and end dates of the best period, along with the maximum gain value found.






 
