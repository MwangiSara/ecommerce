provider "aws" {
  region = "us-east-1"
}

# Security Group
resource "aws_security_group" "django_sg" {
  name = "django_security_group"

  # SSH access restricted to your IP (replace with your IP)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["54.91.142.2/32"] 
  }

  # Allow all inbound traffic
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "my_instance" {
  ami             = "ami-0ebfd941bbafe70c6"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.django_sg.name]

  user_data = <<-EOF
    #!/bin/bash
    sudo yum update -y
    sudo yum install -y python3 python3-pip git

    
    cd /home/ec2-user

    # Clone the Django project
    git clone https://github.com/MwangiSara/ecommerce.git ecommerce

    
    cd ecommerce

    # Set up Python virtual environment
    python3 -m venv env
    source env/bin/activate

    # Install dependencies from requirements.txt
    pip install -r requirements.txt

    # Run Django setup tasks
    python manage.py migrate
    python manage.py collectstatic --noinput

    # Run Django app using Gunicorn
    gunicorn --bind 0.0.0.0:8000 ecommerce.wsgi:application
  EOF

  tags = {
    "Name" = "ecommerce_server"
  }
}
