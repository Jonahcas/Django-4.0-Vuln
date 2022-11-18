# Secure-Code-Demo
My Demo for Secure Coding CSEC 302. It deals with an SQL-Injection vulnerability in certain versions of Python Django (Using 4.0).

While I have set up all the necessary tools within the vm to make the magic happen, here are the steps to create it all from scratch:
1. Create a python venv with: python -m venv [name of virtual env here]
2. Install Django in the venv with: pip install django=4.0
3. Create a project with django-admin startproject [name of project]
4. Add an environment variable with [porjectname].settings in there
