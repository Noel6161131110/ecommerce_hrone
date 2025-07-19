<a id="readme-top"></a>


<h1 align="center">ECommerce HROne</h1>

<p align="center">
  <strong>A sample ecommerce application for HROne.</strong>
</p>

---

## Built With

[![Python][Python-logo]][Python-url] [![FastAPI][FastAPI-logo]][FastAPI-url] [![MongoDB][MongoDB-logo]][MongoDB-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## APIs

- **Create Product [POST]** — Create a product using name, price, and sizes.
- **List Products [GET]** — Retrieve a list of products with optional filters for name and size. Supports pagination using limit and offset for fetching the next page.
- **Create Order [POST]** — Create an order by providing userId and a list of items, each containing a productId and quantity. (Note: Product existence is not validated during order creation.)
- **List of Orders [GET]** — Retrieve all orders, including product details such as name and id. Each order includes a calculated total price, rounded to one decimal place only when there is a fractional part.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



---


## Getting Started

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/Noel6161131110/ecommerce_hrone.git
cd ecommerce_hrone
```

### 2. Create a Python Environment

#### On Unix/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a `.env` file in the root directory with the following content:

```
ENV_MODE=DEVELOPMENT
MONGODB_URI=your_mongodb_connection_url
```

Replace `your_mongodb_connection_url` with your actual MongoDB connection URI.

### 5. Run the Development Server

```bash
fastapi dev src/ --port 8000
```

Make sure to run the above command from the **root** of the project folder.

### 6. Run in Production Mode

```bash
uvicorn src:app --host 0.0.0.0 --port 8000
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



---



## Project Structure

<pre lang="markdown">

```
.
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── app
    │   ├── orders
    │   │   ├── api
    │   │   │   └── controller.py
    │   │   ├── models.py
    │   │   ├── routes.py
    │   │   └── schemas.py
    │   ├── products
    │   │   ├── api
    │   │   │   └── controller.py
    │   │   ├── models.py
    │   │   ├── routes.py
    │   │   └── schemas.py
    │   └── routes.py
    └── database
        └── db.py
```

</pre>



<p align="right">(<a href="#readme-top">back to top</a>)</p>



---


<p align="center"><em>Ecommerce application. With ❤️ open-source.</em></p>





[FastAPI-logo]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/

[Python-logo]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[MongoDB-logo]: https://img.shields.io/badge/-MongoDB-13aa52?style=for-the-badge&logo=mongodb&logoColor=white
[MongoDB-url]: https://www.mongodb.com/
