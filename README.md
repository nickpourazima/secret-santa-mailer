# Secret Santa Mailer

Secret Santa Mailer is a Python script that automates the process of assigning Secret Santa participants and sending them personalized email assignments. It's a fun and efficient way to organize your Secret Santa gift exchange!

## Features

- Randomly assigns participants to each other, ensuring no one gets assigned to themselves or someone from the same group.
- Sends personalized email assignments to participants.
- Easy setup with a JSON configuration file for sender information and participant data.
- Option to save participant assignments to a JSON file.

## Prerequisites

Before using Secret Santa Mailer, make sure you have the following prerequisites installed:

- Python 3.x
- The `smtplib` library for sending emails (typically included with Python)
- Access to a Gmail account for sending emails
- [A Google app password](https://support.google.com/accounts/answer/185833?hl=en)

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/nickpourazima/secret-santa-mailer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd secret-santa-mailer
    ```

3. Create a virtual environment (recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - Windows:

        ```pwsh
        venv\Scripts\activate
        ```

    - macOS and Linux:
  
        ```bash
        source venv/bin/activate
        ```

### Method 1: Using `pip`

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Method 2: Using `setup.py`  

Install the package using setup.py:

```bash
python setup.py install
```

*Note: The setup.py method requires you to have setuptools installed. This method is an alternative to using pip and can be useful if you want to install the package system-wide.*

After completing either of the installation methods, you can proceed to configure and use Secret Santa Mailer as described in the [Configuration](#configuration) and [Usage](#usage) sections

## Configuration

Before running the Secret Santa Mailer script, you need to configure the sender information and participant data.

### Sender Configuration

Edit the sender.json file with your Gmail sender information and a Google Form link ([example](https://docs.google.com/forms/d/e/1FAIpQLSdPlYjnSOcHmqLqH5CbXe_Gn8PbPsXtGZ6SNku_9RvG75LkBQ/viewform?usp=sharing)) for gift preferences:

```json
[
    {
        "sender_email": "your.email@gmail.com",
        "app_password": "your_app_password",
        "google_form": "https://forms.google.com/your_form_link"
    }
]
```

### Participant Data

Edit the participants.json file with the details of your Secret Santa participants. Make sure each participant has a unique name, email (if available), and a group identifier:

```json
[
    {
        "name": "Participant 1",
        "email": "participant1@gmail.com",
        "group": "Group A"
    },
    {
        "name": "Participant 2",
        "email": "participant2@gmail.com",
        "group": "Group B"
    },
    // Add more participants here...
]
```

## Usage

Run the Secret Santa Mailer script to generate and send assignments:

```bash
python secret_santa_mailer.py
```

The script will perform the following steps:

1. Randomly assign participants to each other, ensuring no one gets assigned to themselves or someone from the same group.
2. Send personalized email assignments to each participant.
3. Save participant assignments to a participant_assignments.json file (you can uncomment this option if needed).

## Testing

You can run tests for Secret Santa Mailer using the `pytest` testing framework. Before running the tests, make sure you have installed the required testing dependencies by following the [Installation](#installation) instructions.

To run the tests, execute the following command from the root project directory:

```bash
pytest tests/
```

This command will discover and run all the tests in the project. The tests are located in the tests directory and can be extended to cover additional functionality or custom test cases.

*Note: Ensure that you have the necessary test data and configuration files, such as test_sender.json and test_participants.json, available in the project directory before running the tests. These files should contain test-specific data for your Secret Santa Mailer.*

Feel free to customize and expand the tests in the tests directory to suit your specific use cases and requirements.

By running tests, you can verify the functionality and reliability of Secret Santa Mailer before deploying it in your holiday gift exchange event.

## Disclaimer

This script uses the Gmail SMTP server to send emails. Make sure to follow Google's policies and guidelines when sending emails via SMTP.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Happy Secret Santa organizing!

## Support

If you find Secret Santa Mailer helpful and it adds some holiday magic to your gift exchange event, consider buying me a coffee. Your support helps keep projects like this one going and ensures more festive surprises in the future.

[Buy Me a Coffee](https://ko-fi.com/dillpicholas)

Your generosity is greatly appreciated! 🎅☕
