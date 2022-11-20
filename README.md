# Secure-Code-Demo
My Demo for Secure Coding CSEC 302. It deals with an SQL-Injection vulnerability in certain versions of Python Django (Using 4.0).

## What is Django?
Django is an open-source python web framework that uses a model/template/view architechural pattern. 

## What is the vulnerability?
The vulverability is due to improper string processing when executing SQL.This vulnerability happens in the the ```kind``` function of ```Extract``` and the ```lookup_name``` function of ```Trunc```. Because of this vulnerability, two general exploits are possible:
+ It straight-up makes the program explode (What I'll be demonstrating).
+ It can be used to grab data when applied to a Django web page.

## What was the vulnerable code?
The vulnerable code was more like an *absence* of proper checking, rather than a glaring vulnerability in a function. To remedy this, they implimented a check for common sql injection starters like '

![Both fixes of the code](Old and new code\Comparison 2.PNG)
