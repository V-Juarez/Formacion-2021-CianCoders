import click


@click.group()
def clients():
  """Manages the clients lifecycle"""
  pass


@click.command()
@click.pass_context
def create(ctx, name, company, email, position):
  """Creates a new clients"""
  pass


@click.command()
@click.pass_context
def list(ctx):
  """List all clients"""
  pass


@click.command()
@click.pass_context
def update(ctx, client_uid):
  """Update a clients"""
  pass


@click.command()
@click.pass_context
def delete(ctx, client_uid):
  """Deletes a client"""
  pass


all = clients 

