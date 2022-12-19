# main creds for AWS connection
variable "ecs_cluster" {
  description = "ECS cluster name"
}
variable "ecs_key_pair_name" {
  description = "EC2 instance key pair name"
}
variable "region" {
  description = "AWS region"
}
variable "cluster_vpc_id" {
  description = "VPC name for Test environment"
}
variable "private_subnet_ids" {
  type        = list(string)
  description = "Internal accessible subnet"
}
variable "max_instance_size" {
  description = "Maximum number of instances in the cluster"
}
variable "min_instance_size" {
  description = "Minimum number of instances in the cluster"
}
variable "desired_capacity" {
  description = "Desired number of instances in the cluster"
}
variable "ami_id" {
  description = "ami id of instances in the cluster"
}
variable "cake_office_ip" {
  description = "IP for the office"
}
variable "vpn_ip" {
  description = "IP of the VPN GW"
}
variable "instance_type" {
  description = "instance type for the cluster"
}
variable "volume_type" {
  description = "volume type of the ebs root volume"
}