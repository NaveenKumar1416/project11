DEVOPSFETCH – SERVER INFORMATION RETRIEVAL AND MONITORING TOOL

Overview:
DevOpsfetch is a command-line tool designed for DevOps teams to easily retrieve and monitor system information.
It provides detailed insights about active ports, logged-in users, Nginx configurations, Docker images, and container statuses.
A systemd service can be configured to run this tool continuously for real-time monitoring and logging.

Objectives:
Simplify system information retrieval for DevOps engineers.
Automate continuous monitoring through systemd.
Provide a quick summary of essential system data in one place.

Key Features:
Active Ports and Services Listing (option: -p or --port)
Specific Port Detail Retrieval (option: -p followed by port number)
User Login Information (option: -u or --user)
Nginx Configuration Retrieval (option: -n or --nginx)
Docker Image and Container Status (options: -d or --docker, -c or --container)
Continuous Monitoring with systemd Integration

System Requirements:
Linux environment
Bash shell
systemctl for systemd setup
netstat or ss
docker and nginx if applicable

Installation Steps:
Clone the repository using
git clone https://github.com/yourusername/devopsfetch.git
cd devopsfetch
Make the script executable using
chmod +x devopsfetch.sh
Run the tool using
./devopsfetch.sh -p./devopsfetch.sh --nginx
./devopsfetch.sh -d
