# Serverless Telegram Bot

A basic serverless [Telegram bot](https://core.telegram.org/bots) using [Google Cloud Functions](https://cloud.google.com/functions/).

This bot runs with Python 3.7 and [python-telegram-bot](https://python-telegram-bot.org/).

## Deploy

```
$ gcloud beta functions deploy bot --set-env-vars "TELEGRAM_TOKEN=000:yyy" --runtime python37 --trigger-http
```
