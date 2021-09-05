terraform {
	backend "s3" {
		bucket = "hidoya-terraform-backend"
		key = "tamagotchi"
		region = "us-west-2"
		profile = "home"
	}
}