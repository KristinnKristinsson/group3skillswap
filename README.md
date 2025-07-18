# SkillSwap

## Overview

SkillSwap is a platform for users to learn and teach new skills in a collaborative environment.

## Tech Stack

- Python & Django
- HTML & CSS
- Bootstrap
## Team members

- Asha Mathew
- Kristinn Kristinsson
- Mishkuat Sabir
- Sandhya Kumari
- Shadi Shahsavani

## Prerequisites

- Conda (Anaconda or Miniconda)
- Git
- Python

## Setup Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/KristinnKristinsson/group3skillswap.git
   cd skillswap
   ```

2. **Create and activate a Conda environment**

   ```bash
   conda create -n skillswap_env 
   conda activate skillswap_env
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install pillow
   ```

4. **Configure environment variables**

     -------

5. **Apply database migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py seed
   ```

6. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**

   ```bash
   python manage.py runserver
   ```


## License

This project is licensed under the MIT License.

