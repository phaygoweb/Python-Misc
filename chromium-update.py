#! /usr/bin/python -tt

def main():
  # Root URL to build directory
  rootURL = "http://build.chromium.org/f/chromium/snapshots/chromium-rel-xp/"
  
  # Get latest build number
  data = urllib.request.urlopen(rootURL+"LATEST").read()
  versionNumber = int(data)
  fileMode = str(data)[0]
  
  # Download the latest build
  print("downloading Chromium build", str(versionNumber) + "...")
  chromiumInstaller = urllib.request.urlopen(rootURL+str(versionNumber)+"/mini_installer.exe")

  # Write out installer file
  localFile = open("chromium_latest.exe", "w" + fileMode)
  localFile.write(chromiumInstaller.read())
  localFile.close()

  # Install
  print("Installing...")
  os.system("chromium_latest.exe")

  # Notify of a completed install
  print("Chromium updated to latest build.")
  
  # Log that Chromium was installed
  logging.basicConfig(filename="chromium-installs.log", level=logging.INFO)
  localTime = time.asctime(time.localtime(time.time()))
  logging.info('[' + localTime + '] Chromium ' + str(versionNumber) + ' installed')
  
if __name__ == '__main__':
  import urllib.request
  import os
  import logging
  import time
  
  main()