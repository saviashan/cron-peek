# Cron-Peek

Cron-Peek is a simple but powerful CLI tool designed for developers and DevOps engineers who work with cron schedules. It helps prevent common and costly timezone mistakes by providing a clear forecast of when cron jobs will run in both UTC (server time) and your detected local time.

## The Problem: Timezone Confusion

Cron expressions are almost always defined relative to a server's clock. In modern cloud environments, servers are typically set to UTC. Engineers, however, work in their own local timezones. This discrepancy often leads to "Timezone Confusion," where a cron job scheduled for "midnight" runs at the wrong time from the perspective of the business or the end-user.

For example, a developer in San Francisco (UTC-7) might schedule a job for `0 0 * * *` intending it to run at their midnight, but the server will execute it at UTC midnight—seven hours earlier than expected.

Cron-Peek solves this by showing you exactly what your cron schedule means in both timezones, side-by-side.

## Features

-   **Clear Timezone Comparison**: See the next 5 run times in a table comparing UTC and your local timezone.
-   **Human-Readable Description**: Get a plain-text summary of your cron expression.
-   **Input Validation**: Catches invalid cron expressions and provides a clear error message.
-   **Automatic Timezone Detection**: Your local timezone is detected automatically.

## Installation

You can use `cron-peek` in two ways: directly with Python or via Docker.

### Local Installation (Requires Python 3.10+)

1.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the tool:**
    ```bash
    python main.py "[YOUR_CRON_EXPRESSION]"
    ```
    Example:
    ```bash
    python main.py "*/20 * * * *"
    ```

### Docker Usage

If you have Docker installed, you can run the tool without installing Python or any dependencies on your host machine.

1.  **Build the Docker image:**
    ```bash
    docker build -t cron-peek .
    ```

2.  **Run the tool via Docker:**
    ```bash
    docker run --rm cron-peek "[YOUR_CRON_EXPRESSION]"
    ```
    Example:
    ```bash
    docker run --rm cron-peek "0 18 * * 1-5"
    ```

## Example Usage

Let's say you want to check a cron schedule that runs every 15 minutes.

**Command:**
```bash
python main.py "*/15 * * * *"
```

**Output:**

```
Analysis for: '*/15 * * * *'
Description: Runs according to the schedule: '*/15 * * * *'

                             Next 5 Scheduled Runs
┏━━━┳━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ # ┃ UTC Time (Server Time)  ┃ Local Time                           ┃
┡━━━╇━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1 │ 2024-01-01 12:15:00     │ 2024-01-01 07:15:00 (EST)            │
│ 2 │ 2024-01-01 12:30:00     │ 2024-01-01 07:30:00 (EST)            │
│ 3 │ 2024-01-01 12:45:00     │ 2024-01-01 07:45:00 (EST)            │
│ 4 │ 2024-01-01 13:00:00     │ 2024-01-01 08:00:00 (EST)            │
│ 5 │ 2024-01-01 13:15:00     │ 2024-01-01 08:15:00 (EST)            │
└─-─┴───────────────────────┴──────────────────────────────────────┘
          Times are based on the current system time.
```

## Contributing

Contributions are welcome! If you have ideas for improvements or find a bug, please open an issue or submit a pull request.