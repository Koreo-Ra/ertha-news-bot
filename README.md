# 📰 ertha-news-bot — Telegram bot for monitoring Erthium news

## 🇬🇧 Description

A simple Telegram bot built with `aiogram`, designed to monitor the **[Erthium](https://erthium.medium.com)** Medium blog and send updates to users when a new post mentioning **"Ertha Beta"** appears.

The bot continuously checks the website every 10 seconds and sends you:
- The title of the article (`<h2>`)
- A short description (`<p>`)
- A direct link to the post

Great for keeping your Telegram channel or community up to date with news from the Erthium ecosystem.

---

## 💡 Features
- Monitors the Erthium Medium blog
- Sends updates only when a new post appears (prevents duplicates)
- Automatically removes the `/start` message
- Works asynchronously with `aiogram`
- Sends the post as a formatted message

---

## 🛠 Technologies
- Python 3.10+
- aiogram
- BeautifulSoup (bs4)
- lxml
- requests

---

## 🚀 How to run
1. Clone the repository:
```bash
git clone https://github.com/your-username/ertha-news-bot.git
cd ertha-news-bot
