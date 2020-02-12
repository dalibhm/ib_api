historical_error_value_schema_str = """            
{
   "namespace": "historicalError",
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
     },
     {
        "name" : "errorCode",
        "type" : "int"
     },
     {
        "name" : "errorString",
        "type" : "string"
     }
   ]
}
"""

historical_error_key_schema_str = """
{
   "namespace": "historicalError",
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