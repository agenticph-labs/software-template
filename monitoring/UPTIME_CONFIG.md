# Uptime Robot Configuration

This guide explains how to monitor your deployed application using Uptime Robot.

## Setup Steps

1. **Sign in** to [Uptime Robot](https://uptimerobot.com/).
2. Go to **My Settings** → **Add New Monitor**.
3. Configure as follows:

   | Field          | Value                        |
   |----------------|------------------------------|
   | Monitor Type   | HTTP(s)                      |
   | Friendly Name  | YourApp                      |
   | URL (or IP)    | `https://your-domain.com/health` |
   | Monitoring Interval | 5 minutes            |
   | Timeout        | 30 seconds                   |
   | Alert Contacts | (your email/SMS/Telegram)    |

4. Click **Create Monitor**.

## Expected Health Response

A healthy endpoint returns HTTP `200` with:

```json
{
  "status": "ok",
  "version": "1.0.0",
  "uptime": 12345.67,
  "uptime_human": "3h 25m 45s",
  "db_connected": true,
  "python_version": "3.12.0",
  "platform": "Linux"
}
```

## SSL Certificate Monitoring

Uptime Robot can also monitor SSL certificate expiry. Enable **Monitor SSL certificate** in the advanced settings.

## Alert Configuration

Recommended alert thresholds:

- **Down alert**: After 1 failed check
- **Recovery alert**: After 1 successful check
- **Pause alert after**: 60 minutes of consecutive downtime
