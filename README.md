# SiteSentry

A command-line tool to check the health of a website.

## Installation

1.  Clone the repository:
    ```bash
    git clone git@github.com:saviashan/site-sentry.git
    cd site-sentry
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Check a single URL

```bash
python main.py check [URL]
```

**Example:**

```bash
python main.py check https://www.google.com
```

### Monitor a URL

This will check the URL every 5 seconds until you stop it with `Ctrl+C`.

```bash
python main.py monitor [URL]
```

**Example:**

```bash
python main.py monitor https://www.google.com
```

You can also specify the interval in seconds:

```bash
python main.py monitor https://www.google.com --interval 10
```

## Docker

You can also use Docker to run the application.

1.  Build the Docker image:
    ```bash
    docker build -t sitesentry .
    ```
2.  Run the application:
    ```bash
    docker run --rm sitesentry check https://www.google.com
    ```

    ```bash
    docker run --rm sitesentry monitor https://www.google.com
    ```