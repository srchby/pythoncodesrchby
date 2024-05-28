import cryptography
from cryptography.fernet import Fernet

class PassManager:
  
  def __init__(self):
    self.key = None
    self.pass_file = None
    self.pass_dict = {}

  def cr_key(self, path):
    self.key = Fernet.generate_key()
    with open(path, "wb") as f:
      f.write(self.key)

  def ld_key(self, path):
    with open(path, "rb") as f:
      self.key = f.read()

  def cr_pass_file(self, path, initval=None):
    self.pass_file = path

    if initval is not None:
      for key, value in initval.items():
        self.add_pass(key, value)

  def ld_pass_file(self, path):
    self.pass_file = path

    with open(path, "r") as f:
      for line in f:
        site, encrypted = line.split(":")
        self.pass_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

  def add_pass(self, site, passw):
    self.pass_dict = passw
    
    if self.pass_file is not None:
      with open(self.pass_file, "a+") as f:
        encrypted = Fernet(self.key).encrypt(passw.encode())
        f.write(site + ":" + encrypted.decode() + "\n")

  def get_pass(self, site):
      return self.pass_dict[site]

def main():
  password = {
    
  }