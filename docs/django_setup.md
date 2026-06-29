
# Django Setup Guide

A step-by-step guide to setting up Django on **Windows** and **Linux**, including creating and activating a virtual environment, installing Django, creating a project, and running the development server.

---

# Prerequisites

Before installing Django, ensure you have:

* Python 3.10 or later installed
* pip (Python package manager)
* Command Prompt, PowerShell, or Terminal
* Basic knowledge of the command line

Verify Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

Verify pip installation:

```bash
pip --version
```

---

# Why Use a Virtual Environment?

A **virtual environment (venv)** is an isolated Python environment that keeps project dependencies separate from your system-wide Python installation.

## Importance of Virtual Environment

* Prevents package version conflicts between different projects.
* Keeps project dependencies isolated from the global Python installation.
* Makes projects portable and reproducible.
* Prevents accidental modification of system-wide packages.
* Makes dependency management easier.

Without a virtual environment, installing packages globally can lead to version conflicts and make projects harder to maintain.

---

# Step 1: Create a Project Folder

```bash
mkdir django_project
cd django_project
```

---

# Step 2: Create a Virtual Environment

## Windows

```bash
python -m venv venv
```

## Linux / macOS

```bash
python3 -m venv venv
```

This creates a folder named `venv` that contains an isolated Python environment for your project.

---

# Step 3: Activate the Virtual Environment

## Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

## Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment again:

```powershell
venv\Scripts\Activate.ps1
```

---

## Linux / macOS

```bash
source venv/bin/activate
```

---

## Successful Activation

After activation, your terminal prompt will look similar to:

**Windows**

```text
(venv) C:\django_project>
```

**Linux / macOS**

```bash
(venv) user@ubuntu:~/django_project$
```

The `(venv)` prefix indicates that the virtual environment is active.

---

# Step 4: Upgrade pip (Recommended)

```bash
pip install --upgrade pip
```

---

# Step 5: Install Django

Install Django using pip:

```bash
pip install django
```

Verify the installation:

```bash
django-admin --version
```

Example output:

```text
5.2.3
```

---

# Step 6: Create a Django Project

Run the following command:

```bash
django-admin startproject myproject
```

This creates the following project structure:

```text
myproject/
│
├── manage.py
│
└── myproject/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

---

# Step 7: Navigate to the Project Directory

```bash
cd myproject
```

---

# Step 8: Run the Development Server

Start Django's built-in development server:

```bash
python manage.py runserver
```

By default, Django runs on:

```text
http://127.0.0.1:8000/
```

Open this URL in your web browser. If everything is set up correctly, you will see the Django welcome page.

---

# Running on a Custom Port

To run the server on a different port:

```bash
python manage.py runserver 8080
```

Now access:

```text
http://127.0.0.1:8080/
```

---

# Running on All Network Interfaces

To make the development server accessible on your local network:

```bash
python manage.py runserver 0.0.0.0:8000
```

---

# Deactivate the Virtual Environment

When you finish working on your project, deactivate the virtual environment:

```bash
deactivate
```

---

# Reactivate the Virtual Environment

## Windows

```cmd
venv\Scripts\activate
```

## Linux / macOS

```bash
source venv/bin/activate
```

---

# Summary

1. Install Python.
2. Create a project folder.
3. Create and activate a virtual environment.
4. Upgrade `pip`.
5. Install Django.
6. Create a Django project.
7. Navigate to the project directory.
8. Run the development server.

Using a virtual environment for every Django project ensures clean dependency management, avoids package conflicts, and keeps your development environment organized.
