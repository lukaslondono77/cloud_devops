provider "aws" {
  region = "us-east-1"
}

resource "aws_db_instance" "task_db" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "13.4"
  instance_class       = "db.t3.micro"
  name                 = "taskdb"
  username             = "admin"
  password             = "yourpassword"
  parameter_group_name = "default.postgres13"
  skip_final_snapshot  = true
}

resource "aws_s3_bucket" "task_bucket" {
  bucket = "task-manager-files"
  acl    = "private"
}

resource "aws_eks_cluster" "task_cluster" {
  name     = "task-cluster"
  role_arn = aws_iam_role.eks_cluster.arn

  vpc_config {
    subnet_ids = ["subnet-abc123", "subnet-def456"]
  }
}
