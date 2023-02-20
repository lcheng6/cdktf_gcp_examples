#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, CloudBackend, NamedCloudWorkspace





app = App()
stack = MyStack(app, "cdktf_gcp_examples")
CloudBackend(stack,
  hostname='app.terraform.io',
  organization='example-org-c75662',
  workspaces=NamedCloudWorkspace('cdktf_gcp_examples')
)

app.synth()
