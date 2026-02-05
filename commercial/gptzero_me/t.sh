curl 'https://api.gptzero.me/v2/predict/text' \
    -x http://47.87.143.109:9100 \
  -H 'content-type: application/json' \
  -H 'cookie: accessToken4=eyJhbGciOiJIUzI1NiIsImtpZCI6IkxQUGtRbDRKRlQvcmY5VkoiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNjk1MzEwNzE5LCJpYXQiOjE2OTQ3MDU5MTksImlzcyI6Imh0dHBzOi8vaHR0cHM6Ly9seWRxaGdkemh2c3FsY29iZGZ4aS5zdXBhYmFzZS5jby9hdXRoL3YxIiwic3ViIjoiZGI0Njk2YjktOGE4Mi00MmMxLWI2YjgtYzI0M2I0NWE2MmFhIiwiZW1haWwiOiJkZWdpZml5MzYyQHdpcm91dGUuY29tIiwicGhvbmUiOiIiLCJhcHBfbWV0YWRhdGEiOnsicHJvdmlkZXIiOiJlbWFpbCIsInByb3ZpZGVycyI6WyJlbWFpbCJdfSwidXNlcl9tZXRhZGF0YSI6eyJlbWFpbCI6ImRlZ2lmaXkzNjJAd2lyb3V0ZS5jb20iLCJmdWxsX25hbWUiOiJkZWdpZml5MzYyIiwib3JnIjoiIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoicGFzc3dvcmQiLCJ0aW1lc3RhbXAiOjE2OTQ3MDU5MTl9XSwic2Vzc2lvbl9pZCI6ImRmZDlmM2ZmLTJiMjYtNGE1Ny1iN2Q0LTE3ZmQzZjljZGY1MyJ9.QoqbeC91RgXVYnA2Ca_3f0gZFP2gAaKizSDSzWHvLWc' \
  -H 'origin: https://app.gptzero.me' \
  -H 'referer: https://app.gptzero.me/' \
  --data-raw $'{"document":"More than an AI detector\\nPreserve what\'s human.\\n\\nWe bring transparency to humans navigating a world filled with AI content. GPTZero is the gold standard in AI detection, trained to detect ChatGPT, GPT4, Bard, LLaMa, and other AI models.\\n\\nCheck out our productsand get started\\n"}' \
  --compressed
