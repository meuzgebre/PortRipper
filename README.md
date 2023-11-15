# Port Ripper

Port Ripper is a lightweight and fast port scanning tool designed for basic network analysis. It's focused on speed and simplicity, making it suitable for quick scans of open ports on a target machine.

## Usage

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/meuzgebre/PortRipper.git
    cd PortRipper
    ```

2. **Run the Port Scanner:**

    - To scan a specific port:
        ```bash
        python main.py localhost -p 80
        ```

    - To scan a range of ports:
        ```bash
        python main.py localhost -r 20 100
        ```

    - To scan all ports (1-65535):
        ```bash
        python main.py localhost -a
        ```

## Features

- **Lightweight:** Designed to be a minimalistic and fast port scanning tool.
- **Multi-threaded:** Utilizes threading for faster scans.
- **Command-line Interface:** Easy to use with command-line arguments.
- **Exception Handling:** Handles timeouts and errors gracefully.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
