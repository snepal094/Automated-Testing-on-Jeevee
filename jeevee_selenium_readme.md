# 📄 README.md — Jeevee Selenium Automation Project

## 🧪 Jeevee.com – End-to-End Test Automation (Selenium + Python + PyTest)

This project is an **end-to-end functional UI automation framework** built using **Selenium WebDriver**, **Python**, and **PyTest**, following the **Page Object Model (POM)** design pattern.  
It automates a full user journey on **Jeevee.com**, a Nepal-based e-commerce platform.

This work was completed as the **capstone project** for a QA Automation traineeship program.

---

## 🚀 Features Automated
The project covers a complete real-world shopping flow:

### 🔐 Login
- Expand user profile icon  
- Navigate to login page  
- Enter valid mobile number and password  
- Log into the account  

### 🔍 Search
- Direct search by entering text and pressing ENTER  
- Selecting a product from search results 
- Selecting the first suggestion for search
- Selecting the relevant suggestion for search

### 🛒 Product + Cart Flow
- Open product details page  
- Add product to the cart  
- Open the cart page  

### ⚙️ Cart Actions
- Increase item quantity  
- Decrease item quantity  
- Remove product from cart  
- Proceed to checkout  

This flow represents a **complete smoke test** of the main user journey.

---

## 🏗 Project Structure

```
QA-Project/
│
├── page_objects/
│   ├── login/
│   │   └── LoginLocators.py
│   │   └── LoginProps.py
│   │   └── LoginPage.py
│   │  
│   ├── search/
│   │   └── SearchLocators.py
│   │   └── SearchProps.py
│   │   └── SearchPage.py
│   │  
│   ├── product/
│   │   └── ProductLocators.py
│   │   └── ProductProps.py
│   │   └── ProductPage.py
│   │   
│   └── cart/
│       ├── CartLocators.py
│       └── CartProps.py
│       └── CartPage.py
│
├── setup/
│   └── basetest.py
│
├── creds/
│   └── creds.json
│
├── test cases/
│   ├── test_jeeve.py
│   └── test_search.py
│
└── README.md
```

### 📌 Design Pattern Used  
✔ **Page Object Model (POM)**  
All UI locators and methods are organized logically by page/module:
- `LoginPage` → login actions  
- `SearchPage` → search bar interactions  
- `ProductPage` → product details flow  
- `CartPage` → cart operations  

This ensures clean code, easier debugging, and maximum reusability.

---

## ⚙️ Technologies & Tools
| Component | Description |
|----------|-------------|
| **Language** | Python |
| **Test Framework** | PyTest |
| **Automation Tool** | Selenium WebDriver |
| **Browser** | Google Chrome |
| **Design Pattern** | Page Object Model (POM) |
| **Credential Management** | External JSON file |
| **Logging** | Python logging library |

---

## 🔧 BaseTest – Driver Setup
`BaseTest` handles:
- Initializing Chrome WebDriver  
- Setting Chrome options (disable popups, notifications, password manager)  
- Maximizing window  
- Loading credentials from JSON  
- Opening Jeevee home page  
- Test teardown using `driver.quit()`  

This ensures every test starts on a **clean and stable WebDriver session**.

---

## ▶️ How to Run the Tests

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Add credentials
Place your login credentials inside `creds/creds.json`:
```json
{
  "mobile_num": "98XXXXXXX",
  "password": "yourPassword"
}
```


---

## 🧪 Test Flow (test_jeeve.py)

```python
login = LoginPage(self.driver)
search = SearchPage(self.driver)
product = ProductPage(self.driver)
cart = CartPage(self.driver)

login.profile_icon_expand()
login.login_page()
login.sign_in(self.creds["mobile_num"], self.creds["password"])

direct_search = search.enter_search_text("dot and key sunscreen")
direct_search.send_keys(Keys.ENTER)

product.open_product_page()
cart.add_to_cart_from_product_page()

cart.open_cart_page()
cart.increase_item_count()
cart.decrease_item_count()
cart.remove_from_cart()

cart.checkout()
```

This covers the full **login → search → product → cart → checkout** pipeline.

---

## 🧩 Additional Test Scenarios
Apart from the main demo flow, the project also includes **search functionality test cases** in `test_search.py`:

- Search directly (ENTER key)  
- Select first suggestion from search dropdown  
- Select a suggestion by keyword  

These demonstrate extra test coverage and robustness of the search feature without cluttering the main demo.

---

## 👤 Author
**Suyasha Nepal**  
QA Automation Trainee – Capstone Project

