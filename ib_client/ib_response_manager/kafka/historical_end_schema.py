historical_data_end_value_schema_str = """            
{
   "namespace": "historicalEnd",
   "name": "value",
   "type": "record",
   "fields" : [
     {
       "name" : "symbol",
       "type" : "string"
     },
     {
       "name" : "secType",
       "type" : "string"
     },
     {
       "name" : "currency",
       "type" : "string"
     },
     {
       "name" : "exchange",
       "type" : "string"
     },
     {
       "name" : "start",
       "type" : "string"
     },
     {
       "name" : "end",
       "type" : "string"
     },
     {
       "name" : "barSize",
       "type" : "string"
     },
     {
       "name" : "whatToShow",
       "type" : "string"
     },
     {
       "name" : "useRTH",
       "type" : "int"
     }
   ]
}
"""

historical_data_end_key_schema_str = """
{
   "namespace": "historicalEnd",
   "name": "key",
   "type": "record",
   "fields" : [
     {
       "name" : "requestId",
       "type" : "int"
     }
   ]
}
"""