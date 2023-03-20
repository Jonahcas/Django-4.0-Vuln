# Django-4.0-Demo
My Demo for Secure Coding CSEC 302. It deals with an SQL-Injection vulnerability in certain versions of Python Django (Using 4.0).

## What is Django?
Django is an open-source python web framework that uses a model/template/view architechural pattern. 

## What is the vulnerability?
The vulverability is due to improper string processing when executing SQL.This vulnerability happens in the the ```as_sql``` function of the ```Extract``` class. Because of this vulnerability, two general exploits are possible:
+ It straight-up makes the program explode (What I'll be demonstrating).
+ It can be used to grab data when applied to a Django web page.

## What was the vulnerable code?
The vulnerable code was more like an *absence* of proper checking, rather than a glaring vulnerability in a function. The vulnerability is found in the ```as_sql``` method of the ```ExtractOld``` class, which was pulled from the older, vulnerable version of the code, into the fixed code. The fixed ```Extract``` method still exists and works as intended. (Demonstrate initial test)

ExtractOld: ```django\django\db\models\functions\datetime.py```


To remedy this vulnerability, they implimented a check for valid values of ```lookup_name``` parameter. If the parameter is not a valid ```lookup_name```, then it throws an error. (Demonstrate first fix)

However, this was not the best fix they found for the vulnerability. Instead, they used ***bound variables,*** which allow the addition of parameters into an SQL query without it being interpreted as actual SQL. (Demonstrate second fix)

TL;DR - They fixed it by telling the program "this is a parameter, not actual SQL."


