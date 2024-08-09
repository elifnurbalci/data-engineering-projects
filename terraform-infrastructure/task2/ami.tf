
// Create an EC2 instance with the Amazon Linux AMI using Terraform & attaching existing key-pair "myFirstKey/DE" to the instance

data "aws_ami" "amzn-linux-2023-ami" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023.*-x86_64"]
  }
}

# If you want to add existing VPC, you can either create new subnet for VPC or can use existing subnet_ID of VPC to add it to EC2 instance.
# https://stackoverflow.com/questions/47665428/how-to-launch-ecs-in-an-existing-vpc-using-terraform
# vpc_security_group_ids  -- adding the security group to EC2 instance using id.
# subnet_ID -- this is existing VPC's subnet ID
# key_name -- adding existing keypair to EC2 instance

resource "aws_instance" "web" {
  ami           = data.aws_ami.amzn-linux-2023-ami.id
  instance_type = "t2.micro"
  key_name = "myFirstKey"
  subnet_id = "subnet-0be9d14420cb97600"
  vpc_security_group_ids = [aws_security_group.allow_tls.id]
  tags = {
    Name = "linux-de-elly"
  }

}

# // Assign a VPC to add it to above EC2 instance. 
# If you want to add existing VPC, you can either create new subnet for VPC or can use existing subnet_ID of VPC to add it to EC2 instance.
# https://stackoverflow.com/questions/47665428/how-to-launch-ecs-in-an-existing-vpc-using-terraform
#resource "aws_vpc" "main" {
#  cidr_block = "10.0.0.0/16"
#  
#}


# //Create a new security group. Create a new security group that allows SSH traffic from the internet. 
# //Tip: SSH runs on port 22, and to allow incoming traffic from anywhere CIDR blocks can be set to 0.0.0.0/0.
# //Add the security group to a VPC(vpc_id)
# we have to create egress & ingress rules for new security group.
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = "vpc-0e0c9164b7842bee1"
  tags = {
    Name = "allow_tls"
  }
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.allow_tls.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
  tags = {
     name = "allow_tls outbound rule"
  }
}

resource "aws_vpc_security_group_ingress_rule" "allow_only_port_22" {
  security_group_id = aws_security_group.allow_tls.id
  cidr_ipv4   = "0.0.0.0/0"
  from_port   = 22
  ip_protocol = "tcp"
  to_port     = 22
  tags = {
      name = "allow_tls inbound rule"
  }
}

# //We have a default VPC, that's why we didn't create new one




