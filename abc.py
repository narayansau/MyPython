def AddAMI(template):
    template.add_mapping("RegionMap", {
        "us-east-1": {"AMI": "ami-a4c7edb2"},
        "us-west-2": {"AMI": "ami-6df1e514"},
        "eu-west-1": {"AMI": "ami-327f5352"}
        }
    )

AddAMI("yryr")
