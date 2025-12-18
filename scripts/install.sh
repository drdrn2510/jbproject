
echo "Starting server setup..."


echo "Updating package list..."
if ! sudo apt update;
then
    echo "failed to update package list"
    exit 1
fi

if systemctl status nginx.service exit code 4 >/dev/null 2>&1; then
    echo "Nginx is not installed. Proceeding with installation."
else
    echo "Nginx is already installed. Skipping installation."
    
fi

echo "Installing Nginx..."
if ! sudo apt install -y nginx
then
    echo "failed to install Nginx"
    exit 1
fi
echo "Nginx installed successfully."

echo "Installing pip and pydantic..."
if ! sudo pip install --upgrade pip
then
    echo "failed to upgrade pip"
    exit 1
fi

if ! sudo pip install pydantic
then
    echo "failed to install pydantic"
    exit 1
fi

echo "=== install pydantic done! ==="


if ! sudo systemctl enable nginx;
then
    echo "failed to enable Nginx"
    exit 1
fi

if ! sudo systemctl start nginx;
then
    echo "failed to start Nginx"
    exit 1
fi
echo "nginx is running"


echo "Successful exit..."
exit 0