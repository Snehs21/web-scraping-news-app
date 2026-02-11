# 📰 News Headlines Web Scraper (Streamlit App)

A Python-based **Web Scraping application** that fetches latest news headlines from multiple news websites using **Requests** and **BeautifulSoup**, and displays them using a **Streamlit web interface**. Users can filter headlines by keyword and download results in **CSV or JSON** format.

---

## 🚀 Features

* Scrape headlines from multiple news sources
* Extract **Title, URL, and Source**
* Optional **keyword-based filtering**
* Ethical scraping with **robots.txt check** and request delays
* Interactive **Streamlit UI**
* Download data as **CSV** or **JSON**

---

## 🛠️ Tech Stack

* Python 3
* Streamlit
* Requests
* BeautifulSoup (bs4)
* Pandas

---

## 📁 Project Structure

```
skill ai/web scrapping/
│
├── app.py              # Streamlit UI
├── scraper.py          # Web scraping logic
├── sources.py          # News sources configuration
├── requirements.txt    # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/news-headline-scraper.git
cd news-headline-scraper
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install streamlit requests beautifulsoup4 pandas
```

---

## ▶️ Run the Application

⚠️ Folder name contains spaces, so use quotes:

```powershell
cd "C:\Users\HP\OneDrive\Documents\skill ai\web scrapping"
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧩 Supported News Sources

Configured in `sources.py`:

* BBC News
* CNN

You can easily add more sources by editing `sources.py`.

---

## 📊 Sample Output

| Source | Title                             | URL                                     |
| ------ | --------------------------------- | --------------------------------------- |
| BBC    | Global markets react to inflation | [https://bbc.com/](https://bbc.com/)... |

---

## 🔒 Ethical Scraping

* Respects `robots.txt`
* Adds request delays
* Uses a custom User-Agent

---

## 📌 Resume Highlights

* Web Scraping with BeautifulSoup
* Streamlit Web App Development
* Modular Python Design
* File Handling (CSV & JSON)
* Error Handling & Best Practices

---

## 🔮 Future Enhancements

* Add more news websites
* Show published date/time
* Pagination support
* Deploy on Streamlit Cloud
* User-selectable sources from UI

---

## 👩‍💻 Author

**Sneha Chavan**
Computer Science Engineering Student

---

⭐ If you like this project, don’t forget to star the repository!
