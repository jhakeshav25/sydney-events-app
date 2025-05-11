# Sydney Events App
A minimalistic web application that automatically scrapes and displays events happening in Sydney, Australia.

## 🌟 Features

- Automatically scrapes live events from Eventbrite (specific to Sydney).
- Displays events in a clean, modern layout.
- Collects user email and redirects to original ticket page.
- Automatically updates event listings.

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Scraping:** BeautifulSoup, Requests
- **Frontend:** HTML, CSS (Vanilla)
- **Storage:** JSON

## 🚀 Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jhakeshav25/sydney-events-app.git
   cd sydney-events-app
   ```

2. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Scraper**
   ```bash
   python scraper.py
   ```

5. **Start the Web App**
   ```bash
   python app.py
   ```

6. **Visit in Browser**
   ```
   http://127.0.0.1:5000
   ```

## 📄 License

This project is open-source and free to use under the MIT License.

## 📬 Feedback

Feel free to open issues or pull requests. For suggestions, email:jhakeshav616@gmail.com
