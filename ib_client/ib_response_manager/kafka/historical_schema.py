value_schema_str = """            
{
   "namespace": "historical",
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
       "name" : "date",
       "type" : "string"
     },
     {
       "name" : "open",
       "type" : "double"
     },
     {
       "name" : "high",
       "type" : "double"
     },
     {
       "name" : "low",
       "type" : "double"
     },
     {
       "name" : "close",
       "type" : "double"
     },
     {
       "name" : "volume",
       "type" : "int"
     },
     {
       "name" : "barCount",
       "type" : "int"
     },
     {
       "name" : "average",
       "type" : "double"
     }
   ]
}
"""

key_schema_str = """
{
   "namespace": "historical",
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