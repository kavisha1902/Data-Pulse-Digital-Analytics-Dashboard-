import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///C:/Users/kavis/Desktop/digital-analytics-dashboard/data/analytics.db')

# Pull key metrics
funnel = pd.read_sql("SELECT event_type, COUNT(*) as total FROM ecommerce_events GROUP BY event_type", engine)

views = funnel[funnel['event_type']=='view']['total'].values[0]
carts = funnel[funnel['event_type']=='cart']['total'].values[0]
purchases = funnel[funnel['event_type']=='purchase']['total'].values[0]

top_brand = pd.read_sql("""
    SELECT brand, COUNT(*) as total 
    FROM ecommerce_events 
    WHERE event_type='view' AND brand!='unknown'
    GROUP BY brand ORDER BY total DESC LIMIT 1
""", engine)

summary = f"""
=== Digital Analytics Summary — Nov 2019 ===

Total Views:     {views:,}
Total Carts:     {carts:,}
Total Purchases: {purchases:,}
Conversion Rate: {purchases/views*100:.2f}%

Top Brand: {top_brand['brand'].values[0]} ({top_brand['total'].values[0]:,} views)
"""

print(summary)

# Save summary to file
with open("C:/Users/kavis/Desktop/digital-analytics-dashboard/data/summary_report.txt", "w") as f:
    f.write(summary)

print("Summary saved to data/summary_report.txt")

import smtplib
from email.mime.text import MIMEText

# Email config
SENDER = "kavishasharma1111@gmail.com"
APP_PASSWORD = "vwew pbur rhwh ukyl"  # get from Google
RECEIVER = "kavishasharma1111@gmail.com"

summary = """
=== Digital Analytics Summary — Nov 2019 ===

Total Views:     482,642
Total Carts:     7,763
Total Purchases: 9,595
Conversion Rate: 1.99%

Top Brand: samsung (57,015 views)
"""

msg = MIMEText(summary)
msg['Subject'] = 'Digital Analytics Summary — Nov 2019'
msg['From'] = SENDER
msg['To'] = RECEIVER

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(SENDER, APP_PASSWORD)
    server.send_message(msg)

print("Email sent!")