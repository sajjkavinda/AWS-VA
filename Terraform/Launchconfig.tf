resource "aws_launch_template" "cluster-launch-template" {
  name                                  = "${var.ecs_cluster}-launch-template"
  instance_type                         = var.instance_type
  image_id                              = var.ami_id
  key_name                              = data.aws_key_pair.cluster-key-pair.key_name
  vpc_security_group_ids                = [aws_security_group.cluster-sg.id]
  instance_initiated_shutdown_behavior  = "terminate"


  block_device_mappings {
    device_name = "/dev/sda1"

    ebs {
      volume_size             = 100
      delete_on_termination   = true
      volume_type             = var.volume_type
    }
  }

  iam_instance_profile {
    name = aws_iam_instance_profile.cluster-instance-profile.id
  }

  monitoring {
    enabled = true
  }

  tag_specifications {
    resource_type = "instance"

    tags = {
      Name = "test"
    }
  }

  user_data = ""
}